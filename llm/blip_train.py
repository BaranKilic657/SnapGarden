#!pip install transformers accelerate peft bitsandbytes torchvision
import torch
from transformers import (
    Blip2Processor, 
    Blip2ForConditionalGeneration,
    TrainingArguments,
    Trainer
)
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from PIL import Image

# Load model with memory optimizations
model_name = "Salesforce/blip2-opt-2.7b"
processor = Blip2Processor.from_pretrained(model_name)
model = Blip2ForConditionalGeneration.from_pretrained(
    model_name,
    load_in_8bit=True,  # 8-bit quantization
    device_map="auto",
    torch_dtype=torch.float16
)

# Freeze all parameters except language model
for param in model.vision_model.parameters():
    param.requires_grad = False
for param in model.qformer.parameters():
    param.requires_grad = False
for param in model.language_projection.parameters():
    param.requires_grad = False

# Add LoRA adapters for parameter-efficient training
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    target_modules=["q_proj", "v_proj"]
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Dataset preparation (modify for your dataset)
def process_examples(batch):
    images = [Image.open(img).convert("RGB") for img in batch["image"]]
    inputs = processor(
        images=images,
        text=batch["text"],
        padding="max_length",
        truncation=True,
        max_length=64,
        return_tensors="pt",
    )
    return {
        "pixel_values": inputs.pixel_values,
        "input_ids": inputs.input_ids.squeeze(),
        "attention_mask": inputs.attention_mask.squeeze(),
        "labels": inputs.input_ids.squeeze()
    }

dataset = load_dataset("MakiPan/hagrid250k-blip2")  # Replace with your dataset
processed_ds = dataset.map(process_examples, batched=True, batch_size=8)
train_ds = processed_ds["train"]
eval_ds = processed_ds["validation"]

# Optimized training arguments
training_args = TrainingArguments(
    output_dir="./blip2-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=2,  # Reduce if OOM
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=4,
    evaluation_strategy="steps",
    eval_steps=200,
    save_strategy="steps",
    save_steps=200,
    learning_rate=1e-4,
    weight_decay=0.01,
    fp16=True,
    gradient_checkpointing=True,
    dataloader_num_workers=2,
    remove_unused_columns=True,
    report_to="none",
    optim="adamw_bnb_8bit"  # 8-bit Adam optimizer
)

# Custom data collator
def collate_fn(batch):
    return {
        "pixel_values": torch.stack([x["pixel_values"] for x in batch]),
        "input_ids": torch.stack([x["input_ids"] for x in batch]),
        "attention_mask": torch.stack([x["attention_mask"] for x in batch]),
        "labels": torch.stack([x["labels"] for x in batch])
    }

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    data_collator=collate_fn,
)

# Start training
trainer.train()

# Save final model
model.save_pretrained("./blip2-finetuned")
processor.save_pretrained("./blip2-finetuned")