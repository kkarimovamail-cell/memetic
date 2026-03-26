# Memetic — AI-Powered Meme Generator for SMM

Memetic is an intelligent tool that helps SMM managers, marketers, and small business owners create viral marketing memes in 10 seconds.

Instead of spending hours searching for templates and writing captions, you just enter your **product** and **customer pain** — and Memetic does the rest.

---

## 🚀 Features

- **AI-generated text** — Llama-3 creates witty, context-aware 2-line memes
- **Curated template library** — 10+ meme templates with tags (surprise, fear, joy, etc.)
- **Ready-to-post captions** — includes humor, engagement question, hashtags, and call to action
- **Web interface** — simple, colorful, user-friendly design (yellow/pink/black theme)
- **Telegram bot** — step-by-step conversation: `/start` → product → pain → memes
- **Docker support** — one-command deployment

---

## 🖼️ How It Works
User Input (product + pain)
↓
LLM (Llama-3)
↓
3 Meme Texts Generated
↓
Meme Template Selected (based on tags)
↓
PIL Overlays Text on Image
↓
Output: 3 Memes + Captions


---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI (Python) |
| LLM | Meta Llama-3-8B-Instruct via HuggingFace API |
| Image Processing | Pillow (PIL) |
| Frontend | HTML/CSS/JavaScript |
| Bot | python-telegram-bot |
| Deployment | Docker, Docker Compose |

---

## 🚀 How to Run

### Prerequisites
- Docker and Docker Compose installed
- Git

### 1. Clone the repository
```bash
git clone https://github.com/kkarimovamail-cell/memetic.git
```
```bash
cd memetic
```

