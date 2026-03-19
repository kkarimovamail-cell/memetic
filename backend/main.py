from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm_service import generate_meme_text
from backend.meme_generator import create_meme
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

class MemeRequest(BaseModel):
    product: str
    audience: str
    tone: str

# путь к generated
BASE_DIR = os.path.dirname(__file__)
GENERATED_DIR = os.path.join(BASE_DIR, "generated")

app.mount("/static", StaticFiles(directory=GENERATED_DIR), name="static")

@app.post("/generate")
def generate_meme(request: MemeRequest):

    # 1. текст
    top_text, bottom_text = generate_meme_text(
        request.product,
        request.audience,
        request.tone
    )

    # 2. мем
    filename = create_meme(top_text, bottom_text, request.tone)

    return {
        "top_text": top_text,
        "bottom_text": bottom_text,
        "image": f"/static/{filename}"
    }