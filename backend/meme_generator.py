from PIL import Image, ImageDraw, ImageFont
import random
import os

TEMPLATE_DIR = "backend/templates"
OUTPUT_DIR = "backend/generated"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_meme(top_text, bottom_text):

    template = random.choice(os.listdir(TEMPLATE_DIR))
    template_path = os.path.join(TEMPLATE_DIR, template)

    img = Image.open(template_path)

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("backend/fonts/impact.ttf", 50)

    width, height = img.size

    draw.text(
    (width/2, 50),
    top_text,
    fill="white",
    anchor="mm",
    font=font,
    stroke_width=3,
    stroke_fill="black"
)

    draw.text(
    (width/2, height-50),
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

    return path