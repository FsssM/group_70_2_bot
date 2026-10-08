from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог"), KeyboardButton(text="Контакты"), KeyboardButton(text="Заказать пиццу")]
        # [KeyboardButton(text="Корзина")]  я закоментил так как она попросту ничего не делала, может понадобиться...
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
        [InlineKeyboardButton(text="Наш Instagram", url="https://www.instagram.com/univxrsel?stkn=YnZtbXJhZW9jZnkx&utm_source=qr")],
        [InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")]
    ]
)

