from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from handlers.keyboards import reply_keyboard, inline_keyboard

router_commands = Router()


@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}, я твой первый бот!",
        reply_markup=reply_keyboard
    )
    print(f"Пользователь {message.from_user.full_name} отправил команду /start")


@router_commands.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - перезапуск\n/help - список команд",
        reply_markup=inline_keyboard
    )


@router_commands.message(F.text == "Контакты")
async def show_contacts(message: Message):
    await message.answer("📞 Телефон: +996 555 123 456\n📍 Адрес магазина: г. Бишкек, ул. Ибраимова, 115/1")


@router_commands.message(F.text == "Каталог")
async def show_catalog(message: Message):
    catalog_text = (
        "Наш Каталог:\n\n"
        "1. Ноутбук ASUS — 45 000 сом\n"
        "2. Игровая мышь — 1 500 сом\n"
        "3. Механическая клавиатура — 3 200 сом"
    )
    await message.answer(catalog_text)


@router_commands.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!", show_alert=True)
    
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    quiz_answers = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python", callback_data="quiz_wrong")],
            [InlineKeyboardButton(text="Ubuntu Linux", callback_data="quiz_correct")],
            [InlineKeyboardButton(text="Windows", callback_data="quiz_wrong")]
        ]
    )
    await callback.message.answer("Вопрос: На какой ОС мы работаем по совету учителя? 😎", reply_markup=quiz_answers)


@router_commands.callback_query(F.data == "quiz_correct")
async def quiz_right(callback: CallbackQuery):
    await callback.message.answer("Верно!")
    await callback.answer()


@router_commands.callback_query(F.data == "quiz_wrong")
async def quiz_bad(callback: CallbackQuery):
    await callback.message.answer("Неверно! Попробуйте ещё раз.")
    await callback.answer()


@router_commands.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f'ID этого стикера - {message.sticker.file_id}')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgQAAxkBAANHasjwovX_4jciexabnTfLXO2mIAgAAjQaAAIwDvhTjfmtysL48cw9BA')