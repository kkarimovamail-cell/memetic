from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm_service import generate_meme_text
from backend.meme_generator import create_meme

app = FastAPI()

class MemeRequest(BaseModel):
    product: str
    audience: str
    tone: str

@app.post("/generate")
def generate_meme(request: MemeRequest):

    # 1. Генерируем текст через LLM
    top_text, bottom_text = generate_meme_text(
        request.product,
        request.audience,
        request.tone
    )

    # 2. Генерируем мем
    image_path = create_meme(top_text, bottom_text)

    return {
        "top_text": top_text,
        "bottom_text": bottom_text,
        "image": image_path
    }