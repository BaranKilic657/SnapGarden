from fastapi import FastAPI, File, UploadFile, Form
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
async def analyze_image(file: UploadFile = File(...), question: str = Form(...)):
    """
    Accepts an image and a question, analyzes them, and returns an answer.
    """
    # Open uploaded image and convert it to RGB
    image = Image.open(file.file).convert("RGB")

    # Process the question and image through the model
    inputs = processor(image, question, return_tensors="pt").to("cuda", torch.float16)
    output = model.generate(**inputs)

    # Generate answer
    answer = processor.decode(output[0], skip_special_tokens=True).strip()

    # Return the answer
    return {"answer": answer}
