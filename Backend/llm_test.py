
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from peft import PeftModel


model_name = "Salesforce/blip2-opt-2.7b"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

device = "cpu"
dtype = torch.float32
model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="cpu", torch_dtype=dtype)
torch.set_num_threads(4)  # Adjust based on your CPU's core count
torch.set_num_interop_threads(2)  # Adjust for inter-operation parallelism
model = torch.compile(model, dynamic=False)

image = Image.open("test.jpg").convert("RGB")
question = "Question: What is this plant? Answer:"

inputs = processor(image, question, return_tensors="pt").to(device=device, dtype=dtype)
out = model.generate(
    **inputs,
    max_new_tokens=80,  # Extend from default 30 to ~100 words
)

print(processor.decode(out[0], skip_special_tokens=True).strip())
print(out)
