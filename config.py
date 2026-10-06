from decouple import config
from aiogram import Bot, Dispatcher

BOT_TOKEN = config("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher() 