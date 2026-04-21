from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# TOKEN
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

# LINKS
GAME_URL = "https://notcoin-ten.vercel.app/"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "This is NOT a game about tapping.\n\n"
        "Do nothing — and accept it. Or act — and change it.\n\n"
        "Choose your move."
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Play Game", web_app=WebAppInfo(url=GAME_URL))]
    ])

    await update.message.reply_text(text, reply_markup=keyboard)

# RUN
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()