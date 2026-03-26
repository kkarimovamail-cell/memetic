import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from dotenv import load_dotenv

from backend.llm_service import generate_meme_texts
from backend.meme_generator import create_meme

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

# States for ConversationHandler
PRODUCT, PAIN = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the conversation"""
    await update.message.reply_text(
        "🔥 *Memetic Bot*\n\n"
        "I create memes for SMM marketing!\n\n"
        "Let's start!\n\n"
        "📦 *What is your product or service?*\n"
        "Example: gym, coffee, online course...",
        parse_mode="Markdown"
    )
    return PRODUCT


async def get_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get product from user"""
    product = update.message.text.strip()
    context.user_data['product'] = product

    await update.message.reply_text(
        f"✅ Product: *{product}*\n\n"
        f"😫 *What is the customer pain?*\n"
        f"Example: no motivation, can't wake up, always late...",
        parse_mode="Markdown"
    )
    return PAIN


async def get_pain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get pain and generate memes"""
    pain = update.message.text.strip()
    product = context.user_data.get('product')

    await update.message.reply_text(
        f"🎨 *Generating memes for:*\n"
        f"📦 Product: `{product}`\n"
        f"😫 Pain: `{pain}`\n\n"
        f"⏳ Please wait...",
        parse_mode="Markdown"
    )

    try:
        # Generate 3 meme texts
        texts = generate_meme_texts(product, pain, n=3)

        # Create a meme for each text
        for i, (top_text, bottom_text) in enumerate(texts, 1):
            filename = create_meme(top_text, bottom_text, product)
            image_path = f"backend/generated/{filename}"

            # Prepare social media post
            caption = (
                f"*Meme {i}/3*\n\n"
                f"*Text:*\n"
                f"_{top_text}_\n"
                f"_{bottom_text}_\n\n"
                f"*📢 Social Media Post:*\n"
                f"{top_text}\n{bottom_text}\n\n"
                f"Who relates? 😄 Does this happen to you? Tell us in the comments!\n\n"
                f"🏷 {product} — solves your problem!\n👉 Click the link in bio!\n\n"
                f"#{product.replace(' ', '')} #memes #humor #marketing #advertising #trending"
            )

            with open(image_path, 'rb') as photo:
                await update.message.reply_photo(
                    photo,
                    caption=caption,
                    parse_mode="Markdown"
                )

        # Ask if user wants to continue
        await update.message.reply_text(
            "✨ *Done!*\n\n"
            "Want to create another meme? Send /start",
            parse_mode="Markdown"
        )

    except Exception as e:
        logging.error(f"Error generating meme: {e}")
        await update.message.reply_text(
            "❌ *Generation error!*\n"
            "Please try again later or check your API keys.\n\n"
            "Send /start to try again.",
            parse_mode="Markdown"
        )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the conversation"""
    await update.message.reply_text(
        "❌ *Cancelled.*\n\n"
        "Send /start to begin again.",
        parse_mode="Markdown"
    )
    return ConversationHandler.END


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    await update.message.reply_text(
        "📖 *How to use:*\n\n"
        "1. Send /start\n"
        "2. Enter your product\n"
        "3. Enter the customer pain\n"
        "4. Get 3 memes with ready-to-post captions!\n\n"
        "✨ *Examples:*\n"
        "Product: coffee\n"
        "Pain: can't wake up\n\n"
        "Product: online course\n"
        "Pain: no time to study",
        parse_mode="Markdown"
    )


def main():
    """Start the bot"""
    if not TELEGRAM_TOKEN:
        logging.error("TELEGRAM_BOT_TOKEN not found in .env")
        return

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PRODUCT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_product)],
            PAIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_pain)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("help", help_command))

    logging.info("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()