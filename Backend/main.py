import logging
from fastapi import FastAPI, UploadFile, File, Form
from PIL import Image
import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from peft import PeftModel

# Create FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

model_name = "Salesforce/blip2-opt-2.7b"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

if torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
    base_model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="auto", load_in_8bit=True)
    model = PeftModel.from_pretrained(
                    base_model,
                    "Salesforce/blip2-opt-2.7b",  # Replace with your HF Hub path
                    device_map="auto",
    )
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
async def analyze_image(file: UploadFile = File(...), question: str = Form(...)):
    """
    Accepts an image and a question, analyzes them, and returns an answer.
    """
    # Open uploaded image and convert it to RGB
    image = Image.open(file.file).convert("RGB")
    float_dtype = torch.float16 if device == "cuda" else torch.float32
    
    complete_question = f"Question: {question} Answer:"

    # Process the question and image through the model
    inputs = processor(image, complete_question, return_tensors="pt").to(device=device, dtype=float_dtype)
    
    # Debug: Print the inputs
    logging.debug(f"Inputs: {inputs}")

    out = model.generate(
        **inputs,
        max_new_tokens=80,  # Extend from default 30 to ~100 words
        num_beams=5,         # Better than greedy search
        repetition_penalty=5.0,  # Reduce redundancy
        temperature=0.4,     # Balance creativity/factuality
        early_stopping=True
    )
    print(processor.decode(out[0], skip_special_tokens=True).strip())
    
    # Debug: Print the raw output
    logging.debug(f"Raw output: {out}")

    # Generate answer
    answer = processor.decode(out[0], skip_special_tokens=True).strip()
    
    # Debug: Print the decoded answer
    logging.debug(f"Decoded answer: {answer}")

    # Return the answer
    return {"answer": answer}