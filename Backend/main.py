from fastapi import FastAPI, File, UploadFile, Form
from typing import Optional
import torch
import logging
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from peft import PeftModel

# Create FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

model_name = "Baran657/blip_2_snapgarden"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

if torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
    base_model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="auto", torch_dtype=dtype)
else:
    device = "cpu"
    dtype = torch.float32
    model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="cpu", torch_dtype=dtype)
    torch.set_num_threads(4)  # Adjust based on your CPU's core count
    torch.set_num_interop_threads(2)  # Adjust for inter-operation parallelism
    model = torch.compile(model, dynamic=False)

@app.get("/")
def read_root():
    """
    Root endpoint to test if the API is running.
    """
    return {"message": "Welcome to the SnapGarden API!"}

@app.post("/analyze")
async def analyze_image_or_question(
    file: Optional[UploadFile] = None, 
    question: str = Form(...),
):
    """
    Accepts an image and/or a question, analyzes them, and returns an answer.
    """
    if file:
        # If an image is uploaded, process the image along with the question
        image = Image.open(file.file).convert("RGB")

        inputs = processor(image, question, return_tensors="pt").to(device, dtype=dtype)
    else:
        # If no image is uploaded, only process the question
        inputs = processor(question, return_tensors="pt").to(device, dtype=dtype)

    # Generate model output
    output = model.generate(**inputs)

    # Debug: Print the raw output
    logging.debug(f"Raw output: {output}")

    # Decode the output
    answer = processor.decode(output[0], skip_special_tokens=True).strip()

    # Debug: Print the decoded answer
    logging.debug(f"Decoded answer: {answer}")

    # Assuming the model's answer is a plant name at the beginning (could be adjusted depending on model output)
    plant_name = answer.split(' ')[0]  # Simple approach: assume first word is the plant name
    if not plant_name:
        plant_name = "Unknown Plant"  # Default to "Unknown" if no plant name detected

    # Return the answer and plant name for frontend use
    return {"answer": answer, "plant_name": plant_name}
