import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start_handler
from config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))

    logging.info("Telegram bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
