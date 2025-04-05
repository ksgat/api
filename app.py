from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import random
import io

app = FastAPI()

# Allow access from anywhere (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your 10 classes (customize these as needed)
CLASSES = [
    "cat", "dog", "apple", "car", "phone",
    "tree", "shoe", "book", "cup", "laptop"
]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image
    image_bytes = await file.read()
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception:
        return {"error": "Invalid image file."}

    # Mock prediction: choose random class
    predicted_class = random.choice(CLASSES)

    # Real prediction code placeholder (to uncomment later)
    # input_tensor = transform(image).unsqueeze(0)
    # with torch.no_grad():
    #     outputs = model(input_tensor)
    #     _, predicted = torch.max(outputs, 1)
    #     predicted_class = CLASSES[predicted.item()]

    return {"prediction": predicted_class}
