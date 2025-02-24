from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def level_button():
    button = KeyboardButton(text="LEVEL 1️⃣")
    button2 = KeyboardButton(text="LEVEL 2️⃣")
    button3 = KeyboardButton(text="LEVEL 3️⃣")
    button4 = KeyboardButton(text="LEVEL 4️⃣")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True)
    return rkm


def stop_button():
    button = KeyboardButton(text="🛑 Stop")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True)
    return rkm


def restart_button():
    button = KeyboardButton(text="🎲 Boshlash")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True)
    return rkm

