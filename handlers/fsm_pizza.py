from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class PizzaOrder(StatesGroup):
    size = State()        
    topping = State()     
    address = State()     


router_fsm = Router()

@router_fsm.message(Command('pizza'))
async def start_pizza_fsm(message: Message, state: FSMContext):
    await message.answer("Начинаем заказ пиццы!\nВведите размер пиццы в сантиметрах (например: 30 или 40):")
    await state.set_state(PizzaOrder.size)

@router_fsm.message(F.text == "Заказать пиццу")
async def start_pizza_button(message: Message, state: FSMContext):
    await start_pizza_fsm(message, state)

@router_fsm.message(PizzaOrder.size)
async def process_size(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Ошибка! Размер должен быть числом. Введите размер в см (например: 30):")
        return

    await state.update_data(size=message.text)
    await message.answer("Отлично! Теперь напишите желаемую начинку (например: Пепперони, Сырная):")
    await state.set_state(PizzaOrder.topping)

@router_fsm.message(PizzaOrder.topping)
async def process_topping(message: Message, state: FSMContext):
    await state.update_data(topping=message.text)
    await message.answer("И последнее: введите ваш адрес доставки:")
    await state.set_state(PizzaOrder.address)

@router_fsm.message(PizzaOrder.address)
async def process_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    
    summary_text = (
        "Ваш заказ успешно принят!\n\n"
        f"Размер: {data['size']} см\n"
        f"Начинка: {data['topping']}\n"
        f"Адрес доставки: {data['address']}\n\n"
        "Скоро курьер будет у вас!"
    )
    await message.answer(summary_text)
    await state.clear()
