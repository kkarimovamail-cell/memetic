from PIL import Image, ImageDraw, ImageFont
import random
import os
import json
import textwrap

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "generated")
FONT_PATH = os.path.join(BASE_DIR, "fonts", "impact.ttf")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def wrap_text(text, max_chars=20):
    return "\n".join(textwrap.wrap(text, max_chars))


def load_templates():
    json_path = os.path.join(TEMPLATE_DIR, "templates.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def pick_random_template():
    templates = load_templates()
    return random.choice([t["file"] for t in templates])


def get_font_size(draw, text, img_width, font_path, max_size=60, min_size=20):
    for size in range(max_size, min_size, -2):
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= img_width * 0.9:
            return font

    return ImageFont.truetype(font_path, min_size)


def create_meme(top_text, bottom_text, product):

    template_file = pick_random_template()
    template_path = os.path.join(TEMPLATE_DIR, template_file)

    templates = load_templates()
    if not os.path.exists(template_path):
        print("TEMPLATE NOT FOUND:", template_file)
        template_file = random.choice([t["file"] for t in templates])
        template_path = os.path.join(TEMPLATE_DIR, template_file)

    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    top_text = wrap_text(top_text)
    bottom_text = wrap_text(bottom_text)

    font_top = get_font_size(draw, top_text, width, FONT_PATH)
    font_bottom = get_font_size(draw, bottom_text, width, FONT_PATH)

    draw.text(
        (width / 2, 50),
        top_text,
        fill="white",
        anchor="mm",
        font=font_top,
        stroke_width=3,
        stroke_fill="black"
    )

    draw.text(
        (width / 2, height - 50),
        bottom_text,
        fill="white",
        anchor="mm",
        font=font_bottom,
        stroke_width=3,
        stroke_fill="black"
    )

    filename = f"meme_{random.randint(0,99999)}.png"
    path = os.path.join(OUTPUT_DIR, filename)

    img.save(path)

    return filename