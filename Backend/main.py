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
    # model = torch.compile(model, dynamic=False)
    
def check_plant_name(plant_name):
    """
    Accepted plant names:
        "Cactus"
        "Boston Fern"
        "Basil"
        "Flamingo Flower"
        "Aloe Vera"
        "Elephant Ear"
        "Calathea"
        "Chili Plant"
        "Spider Plant"
        "Citrus Plant"
        "Dumb Cane (Dieffenbachia)"
        "Dragon Tree (Dracaena)"
        "Weeping Fig (Ficus benjamina)"
        "Mint"
        "Monstera"
        "Orchid"
        "Parsley"
        "Philodendron"
        "Pothos"
        "Rosemary"
        "Snake Plant (Sansevieria)"
        "Peace Lily"
        "Succulent"
        "Tomato Plant"
        "ZZ Plant (Zamioculcas zamiifolia)"
    """
    if "Cactus" in plant_name:
        return {True, plant_name}
    else:
        return {False, "Unknown Plant"}

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
    full_question = f"Question: {question} Answer:"
    if file:
        # If an image is uploaded, process the image along with the question
        image = Image.open(file.file).convert("RGB")

        inputs = processor(image, full_question, return_tensors="pt").to(device, dtype=dtype)
    else:
        # If no image is uploaded, only process the question
        inputs = processor(full_question, return_tensors="pt").to(device, dtype=dtype)

    # Generate model output
    output = model.generate(**inputs,
                      max_length=80,
                      repetition_penalty=1.5,
                      length_penalty=1.0)

    # Debug: Print the raw output
    logging.debug(f"Raw output: {output}")

    # Decode the output
    answer = processor.decode(output[0], skip_special_tokens=True).strip()

    # Debug: Print the decoded answer
    logging.debug(f"Decoded answer: {answer}")
    
    is_plant_name, plant_name = check_plant_name(answer)
    
    if not is_plant_name:
        logging.warning(f"Unknown plant name: {plant_name}")
    else:
        logging.info(f"Plant name: {plant_name}")

    # Return the answer and plant name for frontend use
    return {"answer": answer, "plant_name": plant_name}
