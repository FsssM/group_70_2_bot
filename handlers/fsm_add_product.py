from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class add_product(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()


router_add_product = Router()


@router_add_product.message(Command ('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer ('Введите название товара: ')
    await state.set_state(add_product.name)

@router_add_product.message(add_product.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message. answer ('Введите цену товара:')
    await state.set_state(add_product.price)

@router_add_product.message(add_product.price)
async def add_price(message: Message, state: FSMContext):
    await state. update_data(price=message.text)
    await message. answer ('Введите описание товара:')
    await state. set_state(add_product.description)


router_add_product.message(add_product.description)
async def add_description(message: Message, state: FSMContext):
    await state. update_data(description=message.text)
    await message. answer ('Отправьте фото товара:')
    await state. set_state(add_product.photo)


router_add_product.message(add_product.photo)
async def add_photo(message: Message, state: FSMContext):
    await state. update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()

    await message. answer_photo (photo=data['photo'], caption=f"Название: {data['name']}\nЦена: {data['price']}\nОписание: {data['description']}")
    await state.clear()