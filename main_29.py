import sqlite3

products = [
    ('Помидоры', 200),
    ('Огурцы', 300),
    ('Клубника', 500),
    ('Черешня', 600),
    ('Тыква', 100),
    ('Арбуз', 300)

]

with sqlite3.connect("Products1.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER

    )
    """)

    for product in products:
        cur.execute("INSERT INTO products VALUES(NULL, ?, ?)", product)