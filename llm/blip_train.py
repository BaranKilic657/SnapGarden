#!pip install transformers datasets accelerate torchvision peft
import torch
from transformers import (
    Blip2Processor,
    Blip2ForConditionalGeneration,
    TrainingArguments,
    Trainer
)
from datasets import load_dataset
from PIL import Image

# Initialize processor and model
model_id = "sashakunitsyn/vlrm-blip2-opt-2.7b"
processor = Blip2Processor.from_pretrained(model_id)
model = Blip2ForConditionalGeneration.from_pretrained(model_id)

# Uncomment to freeze vision encoder and Q-Former (recommended for limited resources)
# for param in model.vision_model.parameters():
#     param.requires_grad = False
# for param in model.qformer.parameters():
#     param.requires_grad = False

# Load dataset (replace with your dataset)
dataset = load_dataset("ydshieh/coco_dataset_script", "2017", data_dir="./data")
print("Dataset sample:", dataset["train"][0])

def process_items(batch):
    images = [Image.open(img).convert("RGB") for img in batch["image_path"]]
    texts = [t for t in batch["text"]]
    
    inputs = processor(
        images=images,
        text=texts,
        padding="max_length",
        truncation=True,
        max_length=64,
        return_tensors="pt",
    )
    
    return {
        "pixel_values": inputs.pixel_values,
        "input_ids": inputs.input_ids,
        "attention_mask": inputs.attention_mask,
        "labels": inputs.input_ids
    }

# Process dataset
processed_dataset = dataset.map(
    process_items,
    batched=True,
    batch_size=32,
    remove_columns=dataset["train"].column_names
)

# Split dataset
train_ds = processed_dataset["train"]
eval_ds = processed_dataset["validation"]

# Training configuration
training_args = TrainingArguments(
    output_dir="./blip2-opt-2.7b-finetuned",
    num_train_epochs=5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    learning_rate=3e-5,
    weight_decay=0.01,
    fp16=True,
    gradient_checkpointing=True,
    dataloader_num_workers=4,
    remove_unused_columns=False,
    report_to="tensorboard"
)

# Create Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
)

# Start training
train_result = trainer.train()

# Save final model
trainer.save_model("./blip2-opt-2.7b-finetuned")
processor.save_pretrained("./blip2-opt-2.7b-finetuned")

# Evaluation example
sample = eval_ds[0]
image = Image.open(sample["image_path"]).convert("RGB")
inputs = processor(images=image, return_tensors="pt").to("cuda")
generated_ids = model.generate(**inputs, max_length=64)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f"\nGenerated caption: {generated_text}")