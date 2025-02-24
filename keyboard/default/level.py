from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def level_menu():
    button = KeyboardButton(text="Level 1️⃣")
    button2 = KeyboardButton(text="Level 2️⃣")
    button3 = KeyboardButton(text="Level 3️⃣")
    button4 = KeyboardButton(text="Level 4️⃣")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def back_menu():
    button = KeyboardButton(text="⬅️ back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
        ],
        resize_keyboard=True
    )
    return rkm


