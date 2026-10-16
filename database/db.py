# функции для связи с бд
import aiosqlite
from database import queries
from config import path_db

async def init_db():
    async with aiosqlite.connect(path_db) as conn:

        await conn.execute(queries.products_table)
        await conn.execute(queries.products_detail_table)
        
        await conn.execute(queries.create_pizza_table)
        await conn.execute(queries.create_delivery_table)
        
        await conn.commit()
    print('База данных успешно подключена')


async def add_product_db(name, price, description, photo, category, color, product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product, (name, price, photo, product_id))
        await conn.execute(queries.insert_product_detail, (category, color, product_id, description))
        await conn.commit()


async def save_pizza_and_delivery(size: str, topping: str, client_name: str, address: str):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.insert_pizza_order, (size, topping))
        order_id = cursor.lastrowid
        
        await conn.execute(queries.insert_delivery_detail, (order_id, client_name, address))
        await conn.commit()

async def get_all_pizza_orders():
    async with aiosqlite.connect(path_db) as conn:
        conn.row_factory = aiosqlite.Row  
        async with conn.execute(queries.SELECT_ALL_ORDERS_WITH_JOIN) as cursor:
            return await cursor.fetchall()
