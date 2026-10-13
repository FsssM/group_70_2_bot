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

CREATE_PIZZA_TABLE = """
CREATE TABLE IF NOT EXISTS pizza_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT,
    topping TEXT,
    address TEXT
)
"""

INSERT_PIZZA_ORDER = "INSERT INTO pizza_orders (size, topping, address) VALUES (?, ?, ?)"
