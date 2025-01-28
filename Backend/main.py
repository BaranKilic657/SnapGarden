from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from typing import Optional
import torch
import logging
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace "*" with your frontend URL in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

model_name = "Baran657/blip_2_snapgarden"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

# Initialize device and model
if torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
    logging.debug("CUDA is available; using GPU.")
    model = Blip2ForConditionalGeneration.from_pretrained(
        model_name, device_map="auto", torch_dtype=dtype
    )
else:
    device = "cpu"
    dtype = torch.float32
    logging.debug("CUDA is not available; using CPU.")
    model = Blip2ForConditionalGeneration.from_pretrained(
        model_name, device_map="cpu", torch_dtype=dtype
    )
    # Adjust threads for CPU performance if desired
    torch.set_num_threads(4)
    torch.set_num_interop_threads(2)
    # model = torch.compile(model, dynamic=False)  # Optional: for PyTorch 2.x

def check_plant_name(plant_name: str):
    """
    Quick verification if recognized name is in the known plant list.
    Return (True, plant_name) if recognized, else (False, 'Unknown Plant').
    """
    known_plants = [
        "Aloe vera",
        "Basil",
        "Boston fern",
        "Calathea",
        "Cactus",
        "Chili Plant",
        "Citrus Plant",
        "Dumb Cane (Dieffenbachia)",
        "Dragon Tree (Dracaena)",
        "Elephant Ear",
        "Fern",
        "Flamingo Flower",
        "Maple",
        "Mint",
        "Monstera",
        "Oak",
        "Orchid",
        "Parsley",
        "Peace Lily",
        "Philodendron",
        "Pothos",
        "Rosemary",
        "Rose",
        "Snake Plant (Sansevieria)",
        "Spider Plant",
        "Succulent",
        "Sunflower",
        "Tomato Plant",
        "Tulip",
        "Weeping Fig (Ficus Benjamina)",
        "ZZ Plant (Zamioculcas Zamiifolia)"
    ]

    # Simple containment check (case-insensitive)
    for kp in known_plants:
        if plant_name.lower() == kp.lower():
            return (True, kp)
    return (False, "Unknown Plant")

@app.get("/")
def read_root():
    """
    Root endpoint to test if the API is running.
    """
    return {"message": "Welcome to the SnapGarden API!"}

@app.post("/analyze")
async def analyze_image_or_question(
    file: Optional[UploadFile] = File(None),
    question: str = Form("Identify the plant in the image. Return only the plant name with no extra words.")
):
    """
    Accepts an image and/or a question, analyzes them, and returns an answer + recognized plant name.
    """
    try:
        # Validate the uploaded file (if provided)
        image = None
        if file:
            if not file.content_type.startswith("image/"):
                raise HTTPException(
                    status_code=400, detail="Uploaded file must be an image."
                )
            try:
                logging.debug(f"File content type: {file.content_type}")
                logging.debug(f"File size: {file.size if hasattr(file, 'size') else 'Unknown'}")
                image = Image.open(file.file).convert("RGB")
                logging.debug("Image successfully opened and converted to RGB.")
            except Exception as e:
                logging.error(f"Error opening image: {str(e)}")
                raise HTTPException(
                    status_code=400, detail="Invalid or corrupted image file."
                )

        # Provide a more direct prompt for the model
        # e.g., "Identify exactly which plant is in the image. Nothing else. e.g. 'Aloe Vera'."
        prompt = f"Question: {question} Answer:"
        logging.debug(f"Prompt sent to the model: {prompt}")

        # Prepare inputs for the model
        if image:
            inputs = processor(image, prompt, return_tensors="pt").to(device, dtype=dtype)
        else:
            # If no image is provided, only process the question
            inputs = processor(text=prompt, return_tensors="pt").to(device, dtype=dtype)

        # Generate model output
        output = model.generate(
            **inputs,
            max_length=80,
            repetition_penalty=1.5,
            length_penalty=1.0
        )

        # Decode the output
        answer = processor.decode(output[0], skip_special_tokens=True).strip()
        logging.debug(f"Decoded answer from model: {answer}")

        # Extract a final plant name
        plant_name = extract_plant_name(answer)
        if not plant_name:
            plant_name = "Unknown Plant"

        # Return the raw model answer and the extracted plant name
        return {"answer": answer, "plant_name": plant_name}

    except Exception as e:
        logging.error(f"Error during analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")


def extract_plant_name(answer: str) -> str:
    """
    Extracts the plant name from the model's answer by scanning known keywords.
    If none are found, returns the entire answer verbatim (for debugging),
    and then check if it's recognized with `check_plant_name`.
    """
    if not answer:
        return "Unknown Plant"

    # Known plant keywords (lowercase)
    plant_keywords = [
        "aloe vera",
        "aloe",
        "basil",
        "boston fern",
        "calathea",
        "cactus",
        "chili plant",
        "citrus plant",
        "dumb cane (dieffenbachia)",
        "dragon tree (dracaena)",
        "elephant ear",
        "fern",
        "flamingo flower",
        "maple",
        "mint",
        "monstera",
        "oak",
        "orchid",
        "parsley",
        "peace lily",
        "philodendron",
        "pothos",
        "rosemary",
        "rose",
        "snake plant (sansevieria)",
        "spider plant",
        "succulent",
        "sunflower",
        "tomato plant",
        "tulip",
        "weeping fig (ficus benjamina)",
        "zz plant (zamioculcas zamiifolia)"
    ]
    answer_lower = answer.lower()

    # Attempt to extract by scanning keywords
    detected_plant = None
    for keyword in plant_keywords:
        if keyword in answer_lower:
            # Return the keyword in title case (e.g., "Aloe Vera")
            # or refine if you want a specific capitalization
            detected_plant = keyword.title()
            break

    # If we found a keyword, let's see if it's recognized in check_plant_name
    if detected_plant:
        is_known, final_plant = check_plant_name(detected_plant)
        if is_known:
            return final_plant  # returns the properly capitalized version
        else:
            logging.warning(f"Detected {detected_plant} but not in known_plants list.")
            return "Unknown Plant"

    # If no keyword match, fallback to the entire answer to see if it's recognized
    is_known, final_plant = check_plant_name(answer.strip())
    if is_known:
        return final_plant

    # If still not recognized, return a truncated or full answer for debugging
    logging.warning(f"No known plant keyword found in: {answer}")
    return answer.strip()  # Or: "Unknown Plant"


# Run the app (for development / debugging only)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)