from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import aiosqlite
from config import path_db

router_delete = Router()

class EditProduct(StatesGroup):
    new_name = State()
    new_price = State()

@router_delete.message(Command('edit'))
async def check_staff_access(message: Message):
    ADMIN_ID = 781280469
    
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ У вас нет доступа к этой команде! Вы не являетесь администратором.")
        return
        
    async with aiosqlite.connect(path_db) as conn:
        conn.row_factory = aiosqlite.Row
        async with conn.execute("SELECT id, name, price, product_id FROM products") as cursor:
            products = await cursor.fetchall()
            
    if not products:
        await message.answer("В базе пока нет товаров для редактирования.")
        return

    await message.answer("Доступ разрешен, Администратор. Список товаров магазина:")
    
    for row in products:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Изменить", callback_data=f"edit_start_{row['product_id']}"),
                    InlineKeyboardButton(text="Удалить", callback_data=f"delete_{row['product_id']}")
                ]
            ]
        )
        
        await message.answer(
            text=f"**Товар:** {row['name']}\n**Цена:** {row['price']} сом\n**Артикул:** {row['product_id']}",
            reply_markup=keyboard
        )

@router_delete.callback_query(F.data.startswith('delete_'))
async def process_delete_product(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        await conn.execute("DELETE FROM products_detail WHERE product_id = ?", (product_id,))
        await conn.commit()
        
    await callback.message.edit_text(f"Товар с артикулом `{product_id}` успешно удален!")
    await callback.answer("Товар удален", show_alert=True)

@router_delete.callback_query(F.data.startswith('edit_start_'))
async def start_edit_product(callback: CallbackQuery, state: FSMContext):
    product_id = callback.data.split('_')[2]
    await state.update_data(edit_product_id=product_id)
    
    await callback.message.answer(f"Меняем товар с артикулом {product_id}.\nВведите НОВОЕ НАЗВАНИЕ товара:")
    await state.set_state(EditProduct.new_name)
    await callback.answer()

@router_delete.message(EditProduct.new_name)
async def process_edit_name(message: Message, state: FSMContext):
    await state.update_data(new_name=message.text)
    await message.answer("Теперь введите НОВУЮ ЦЕНУ товара:")
    await state.set_state(EditProduct.new_price)

@router_delete.message(EditProduct.new_price)
async def process_edit_price(message: Message, state: FSMContext):
    await state.update_data(new_price=message.text)
    data = await state.get_data()
    
    product_id = data['edit_product_id']
    new_name = data['new_name']
    new_price = data['new_price']
    
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(
            "UPDATE products SET name = ?, price = ? WHERE product_id = ?",
            (new_name, new_price, product_id)
        )
        await conn.commit()
        
    await message.answer(
        f"✅ Данные успешно обновлены в базе через UPDATE!\n\n"
        f"Артикул: {product_id}\n"
        f"Новое название: {new_name}\n"
        f"Новая цена: {new_price} сом"
    )
    await state.clear()