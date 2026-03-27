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
### 2. Create .env file
Create a file named .env in the project root and add your API keys:
```bash
HF_API_KEY=your_huggingface_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```
Where to get the keys:

HuggingFace API key: https://huggingface.co/settings/tokens (type: Read)

Telegram Bot Token: Create a bot via @BotFather and copy the token

### 3. Run with Docker
```bash
docker-compose up --build
```
### 4. Open the website
http://127.0.0.1:8000

### 5. Try the Telegram bot
Find your bot on Telegram and send 
/start

📱 Usage Examples

Web Interface

1. Enter Product (e.g., gym)
2. Enter Pain (e.g., no motivation)
3. Click Generate
4. Get 3 memes + ready-to-post captions
5. Click Copy All — paste into social media

🧪 Example Output

#### Input:
Product: gym

Pain: no motivation

#### Generated:

Meme 1: "Gym membership paid / Still on couch"

Meme 2: "Bought workout gear / Only wear to store"

Meme 3: "Downloaded fitness app / Only opened once"

Each comes with a caption:

```bash
Who relates? 😄 Does this happen to you? Tell us in the comments!

🏷 gym — solves your problem!
👉 Click the link in bio!

#gym #memes #humor #marketing #advertising #trending
```

