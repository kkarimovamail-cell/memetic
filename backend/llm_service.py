import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


def generate_meme_text(product, audience, tone):

    prompt = f"""
Create text for a marketing meme.

Product: {product}
Audience: {audience}
Tone: {tone}

Return format:

Top: ...
Bottom: ...
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 50
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    result = response.json()

    # Если модель вернула нормальный ответ
    if isinstance(result, list) and "generated_text" in result[0]:

        text = result[0]["generated_text"]

        try:
            top = text.split("Top:")[1].split("Bottom:")[0].strip()
            bottom = text.split("Bottom:")[1].strip()
        except:
            top = "Когда запускаешь рекламу"
            bottom = "И ждёшь клиентов"

    else:
        # fallback если HF не ответил
        top = "Когда запускаешь рекламу"
        bottom = "И ждёшь клиентов"

    return top, bottom