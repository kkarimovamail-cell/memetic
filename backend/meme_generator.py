from PIL import Image, ImageDraw, ImageFont
import random
import os
import json

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "generated")
FONT_PATH = os.path.join(BASE_DIR, "fonts", "impact.ttf")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_templates():
    json_path = os.path.join(TEMPLATE_DIR, "templates.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def pick_template(tone):
    templates = load_templates()

    # ищем по тегу
    for t in templates:
        if tone.lower() in [tag.lower() for tag in t["tags"]]:
            return t["file"]

    # fallback
    return random.choice([t["file"] for t in templates])


def create_meme(top_text, bottom_text, tone):

    template_file = pick_template(tone)
    template_path = os.path.join(TEMPLATE_DIR, template_file)

    img = Image.open(template_path)

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FONT_PATH, 50)

    width, height = img.size

    # верхний текст
    draw.text(
        (width / 2, 50),
        top_text,
        fill="white",
        anchor="mm",
        font=font,
        stroke_width=3,
        stroke_fill="black"
    )

    # нижний текст
    draw.text(
        (width / 2, height - 50),
        bottom_text,
        fill="white",
        anchor="mm",
        font=font,
        stroke_width=3,
        stroke_fill="black"
    )

    filename = f"meme_{random.randint(0,99999)}.png"
    path = os.path.join(OUTPUT_DIR, filename)

    img.save(path)

    return filename