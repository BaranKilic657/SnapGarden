
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from peft import PeftModel


model_name = "Baran657/blip_2_snapgarden"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

device = "cpu"
dtype = torch.float32
model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="cpu", torch_dtype=dtype)

torch.set_num_threads(4)  # Adjust based on your CPU's core count
torch.set_num_interop_threads(2)  # Adjust for inter-operation parallelism
model = torch.compile(model, dynamic=False)

image = Image.open("path").convert("RGB")
image.resize((334,334), Image.Resampling.LANCZOS)
question = "Question: Is this plant healthy? Answer:"

inputs = processor(image, question, return_tensors="pt").to(device=device, dtype=dtype)
out = model.generate(**inputs,
                      max_length=80,
                      repetition_penalty=1.5,
                      length_penalty=1.0)

print(processor.decode(out[0], skip_special_tokens=True).strip())
print(out)
