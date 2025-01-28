from fastapi import FastAPI, File, UploadFile, Form
from typing import Optional
import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

# Create FastAPI app
app = FastAPI()

# Load AI model and processor
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", load_in_8bit=True, device_map="auto")

@app.get("/")
def read_root():
    """
    Root endpoint to test if the API is running.
    """
    return {"message": "Welcome to the SnapGarden API!"}

@app.post("/analyze")
async def analyze_image_or_question(
    file: Optional[UploadFile] = None, 
    question: str = Form(...)
):
    """
    Accepts an image and/or a question, analyzes them, and returns an answer.
    """
    if file:
        # Process the uploaded image
        image = Image.open(file.file).convert("RGB")
        inputs = processor(image, question, return_tensors="pt").to("cuda", torch.float16)
    else:
        # Process only the question
        inputs = processor(question, return_tensors="pt").to("cuda", torch.float16)

    # Generate model output
    output = model.generate(**inputs)

    # Generate answer
    answer = processor.decode(output[0], skip_special_tokens=True).strip()

    # Return the answer
    return {"answer": answer}
