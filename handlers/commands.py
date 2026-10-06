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

    print(f"Пользователь {message.from_user.full_name} под ником {message.from_user.username} отправил команду /start")


@router_commands.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - привествие\n"
        "/help - список команд",
        reply_markup=inline_keyboard
    )

@router_commands.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer(f"Добавлена в корзину!!!")

@router_commands.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!!!", show_alert=True)
    await callback.message.answer("Первый вопрос: Второй закон Ньютона?")
