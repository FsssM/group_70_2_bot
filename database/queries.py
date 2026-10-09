# sql запросы 

products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        price INTEGER,
        description TEXT,
        photo TEXT
    )
"""


insert_product = "INSERT INTO products (name, price, description, photo) VALUES (?, ?, ?, ?)"