from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_keyboard

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="Hello! This is an automated Telegram bot 🤖",
        reply_markup=main_keyboard()
    )
