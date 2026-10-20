# sql запросы 

products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        price INTEGER,
        photo TEXT,
        product_id INTEGER NOT NULL UNIQUE
    )
"""

insert_product = "INSERT INTO products (name, price, photo, product_id) VALUES (?, ?, ?, ?)"
products_detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        color TEXT,
        product_id INTEGER NOT NULL UNIQUE,
        description TEXT
    )
"""
insert_product_detail = "INSERT INTO products_detail (category, color, product_id, description) VALUES (?, ?, ?, ?)" 
# products.product_id = products_detail.product_id 


CREATE_PIZZA_TABLE = """
CREATE TABLE IF NOT EXISTS pizza_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT,
    topping TEXT,
    address TEXT
)
"""

INSERT_PIZZA_ORDER = "INSERT INTO pizza_orders (size, topping, address) VALUES (?, ?, ?)"

create_pizza_table = """
CREATE TABLE IF NOT EXISTS pizza_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT,
    topping TEXT
)
"""


create_delivery_table = """
CREATE TABLE IF NOT EXISTS delivery_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    client_name TEXT,
    address TEXT,
    FOREIGN KEY (order_id) REFERENCES pizza_orders(order_id)
)
"""


insert_pizza_order = "INSERT INTO pizza_orders (size, topping) VALUES (?, ?)"
insert_delivery_detail = "INSERT INTO delivery_details (order_id, client_name, address) VALUES (?, ?, ?)"


SELECT_ALL_ORDERS_WITH_JOIN = """
SELECT p.size, p.topping, d.client_name, d.address 
FROM pizza_orders p
INNER JOIN delivery_details d ON p.order_id = d.order_id
"""

DELETE_PRODUCT = "DELETE FROM products WHERE product_id = ?"
DELETE_PRODUCT_DETAIL = "DELETE FROM products_detail WHERE product_id = ?"
