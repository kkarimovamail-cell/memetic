from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.llm_service import generate_meme_texts
from backend.meme_generator import create_meme

app = FastAPI()


class MemeRequest(BaseModel):
    product: str
    pain: str


app.mount("/static", StaticFiles(directory="backend/generated"), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")


@app.post("/generate")
def generate_meme(request: MemeRequest):

    texts = generate_meme_texts(
        request.product,
        request.pain,
        n=3
    )

    memes = []

    for top_text, bottom_text in texts:
        filename = create_meme(top_text, bottom_text, request.product)

        memes.append({
            "top_text": top_text,
            "bottom_text": bottom_text,
            "product": request.product,
            "pain": request.pain,
            "image": f"/static/{filename}"
        })

    return memes