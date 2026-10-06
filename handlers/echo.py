from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

router_echo = Router()

@router_echo.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

