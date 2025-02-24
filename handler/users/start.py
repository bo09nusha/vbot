from aiogram import Bot, Router, types, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
import random
from states.level import LevelState
from keyboard.default.level_keyboard import level_button

router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!",
                         reply_markup=level_button())
    await message.answer_photo("https://telegra.ph/file/8b13919c076e881fde66b.png",
                               caption=f"Hush kelibsiz {message.from_user.first_name} "
                                       f"bilag'on, \nsizga bir nechta savolar berib "
                                       f"bilimingizni tekshirib beramiz!")
    await state.set_state(LevelState.level)


@router.message(LevelState.level)
async def lvl_handler(message: types.Message, state: FSMContext):
    if message.text == "LEVEL 1️⃣":
        question = f"{random.randrange(1, 11)} {random.choice(['+', '-', '*'])} {random.randrange(1, 11)}"

    answer = eval(question)
    await state.update_data(answer=answer, level=message.text, true=0, false=0)
    await message.answer(f"SAVOL : {question}  = ?")
    await state.set_state(LevelState.answer)


@router.message(StateFilter(LevelState.answer))
async def start_test(message: types.Message, state: FSMContext):
    data = await state.get_data()

    user_answer = int(message.text)
    correct_answer = data.get("answer")

    if user_answer == correct_answer:
        await message.answer("✅ To'g'ri!")
    else:
        await message.answer(f"❌ Noto'g'ri! To'g'ri javob: {correct_answer}")

    if data.get("level") == "LEVEL 1️⃣":
        question = f"{random.randrange(1, 11)} {random.choice(['+', '-', '*'])} {random.randrange(1, 11)}"

    answer = eval(question)
    await state.update_data(answer=answer)
    await state.set_state(LevelState.answer)
    await message.answer(f"SAVOL: {question}  = ?")








@router.message(F.text == "🎲 Boshlash")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"O'yin qaytadan boshlandi!",
                         reply_markup=level_button())
    await state.set_state(LevelState.level)


