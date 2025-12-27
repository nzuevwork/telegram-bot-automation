from telegram import ReplyKeyboardMarkup

def main_keyboard():
    keyboard = [
        ["📊 Status", "⚙ Settings"],
        ["❓ Help"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
