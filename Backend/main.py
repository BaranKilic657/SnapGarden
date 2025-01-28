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

# Model name (BLIP-2)
model_name = "Salesforce/blip2-opt-2.7b"

# Load AI model and processor
processor = Blip2Processor.from_pretrained(model_name)

# Initialize device and model
if torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
    model = Blip2ForConditionalGeneration.from_pretrained(
        model_name, device_map="auto", load_in_8bit=True
    )
else:
    device = "cpu"
    dtype = torch.float32
    model = Blip2ForConditionalGeneration.from_pretrained(
        model_name, device_map="cpu", torch_dtype=dtype
    )
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
    file: Optional[UploadFile] = File(None), 
    question: str = Form(...),
):
    """
    Accepts an image and/or a question, analyzes them, and returns an answer.
    """
    try:
        # Validate the uploaded file (if provided)
        if file:
            if not file.content_type.startswith("image/"):
                raise HTTPException(
                    status_code=400, detail="Uploaded file must be an image."
                )
            try:
                logging.debug(f"File content type: {file.content_type}")
                logging.debug(f"File size: {file.size}")
                image = Image.open(file.file).convert("RGB")
                logging.debug("Image successfully opened and converted to RGB.")
            except Exception as e:
                logging.error(f"Error opening image: {str(e)}")
                raise HTTPException(
                    status_code=400, detail="Invalid or corrupted image file."
                )
        else:
            image = None

        # Prepare inputs for the model
        if image:
            inputs = processor(image, question, return_tensors="pt").to(device, dtype=dtype)
        else:
            # If no image is provided, only process the question
            inputs = processor(text=question, return_tensors="pt").to(device, dtype=dtype)

        # Generate model output
        output = model.generate(**inputs)

        # Decode the output
        answer = processor.decode(output[0], skip_special_tokens=True).strip()

        # Debug: Print the decoded answer
        logging.debug(f"Decoded answer: {answer}")

        # Extract plant name (improved logic)
        plant_name = extract_plant_name(answer)
        if not plant_name:
            plant_name = "Unknown Plant"  # Default to "Unknown" if no plant name detected

        # Return the answer and plant name for frontend use
        return {"answer": answer, "plant_name": plant_name}

    except Exception as e:
        logging.error(f"Error during analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during analysis.")

def extract_plant_name(answer: str) -> str:
    """
    Extracts the plant name from the model's answer.
    This is a placeholder function and can be improved based on the model's output format.
    """
    # Example: If the answer is "This is a rose plant.", extract "rose"
    # You can replace this with a more sophisticated method (e.g., NER, keyword matching)
    keywords = ["rose", "tulip", "sunflower", "oak", "maple"]  # Add more plant names
    for keyword in keywords:
        if keyword in answer.lower():
            return keyword.capitalize()
    return ""

# Run the app (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)