# функции для связи с бд
import sqlite3
from database import queries

path_db = "database/sqlite3.db"

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.products_table)
    print('DB connect')
    conn.commit()
    conn.close()

def add_product_db(name, price, description, photo):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name, price, description, photo))
    # cursor.execute(queries.insert_product, (name,))
    conn.commit()
    conn.close()