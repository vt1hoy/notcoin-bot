from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
# =========================
# ВСТАВЬ СЮДА СВОЙ ТОКЕН
# =========================
TOKEN = os.getenv("8627931912:AAEOh-io-RmCVuGuCy6DeKG3jSthb_qATpw")

# =========================
# ССЫЛКИ
# =========================
GAME_URL = "https://notcoin-ten.vercel.app/"
COMMUNITY_URL = "https://t.me/yourcommunity"   # поменяй
CHANNEL_URL = "https://t.me/yourchannel"       # поменяй

# =========================
# /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Hello, fren.\n\n"
        "Notcoin is no longer just a tap.\n"
        "Now it is hype, trust, builders and holders.\n\n"
        "Choose your path."
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Play Game", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton("🤝 Join Community", url=COMMUNITY_URL)],
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_URL)],
    ])

    await update.message.reply_text(text, reply_markup=keyboard)

# =========================
# ЗАПУСК
# =========================
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()