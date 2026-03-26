import os
import requests
from dotenv import load_dotenv
import random
import re


load_dotenv()

API_URL = "https://router.huggingface.co/v1/chat/completions"
API_KEY = os.getenv("HF_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
}


def clean_text(text: str) -> str:
    text = re.sub(r"[^\w\s.,!?-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_to_two_lines(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    if len(lines) >= 2:
        return lines[0], lines[1]

    if len(lines) == 1:
        words = lines[0].split()
        mid = len(words) // 2 or 1
        return " ".join(words[:mid]), " ".join(words[mid:])

    return None, None


def generate_one_meme_text(product, pain):

    prompt = f"""
You are a viral meme generator for SMM marketing.

STRICT RULES:
- EXACTLY 2 lines
- MAX 6 words per line
- Make a funny meme about {product} that addresses this customer pain: "{pain}"
- Be witty, relatable, and make people laugh
- Respond ONLY with two lines, no explanations

Examples:
Product: gym, Pain: no motivation to workout
Gym membership paid
Still on the couch

Product: coffee, Pain: can't wake up
Alarm at 7am
Me at 7am

Now generate for {product} with pain: {pain}
"""

    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct:novita",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 1.1,
        "max_tokens": 40
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        result = response.json()

        print("LLAMA RESPONSE:", result)

        text = result["choices"][0]["message"]["content"]
        text = clean_text(text)

        top, bottom = split_to_two_lines(text)

        if top and bottom:
            return top, bottom

    except Exception as e:
        print("LLM ERROR:", e)

    # English fallback memes
    fallbacks = [
        ("Signed up for gym", "Still on couch"),
        ("Bought workout gear", "Only wear to store"),
        ("Found perfect course", "Never opened it"),
        ("Ordered healthy meal", "Ate chips instead"),
        ("Downloaded fitness app", "Only opened once"),
    ]
    return random.choice(fallbacks)


def generate_meme_texts(product, pain, n=3):
    results = []

    for _ in range(n):
        top, bottom = generate_one_meme_text(product, pain)
        results.append((top, bottom))

    return results