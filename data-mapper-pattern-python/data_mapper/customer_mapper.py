import sqlite3
from domain.customer import Customer

class CustomerMapper:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
        """)
        self.conn.commit()

    def insert(self, customer: Customer):
        cursor = self.conn.execute(
            "INSERT INTO customers (name, email) VALUES (?, ?)",
            (customer.name, customer.email)
        )
        customer.id = cursor.lastrowid
        self.conn.commit()

    def find_by_id(self, customer_id: int) -> Customer:
        cursor = self.conn.execute(
            "SELECT id, name, email FROM customers WHERE id = ?",
            (customer_id,)
        )
        row = cursor.fetchone()
        if row:
            return Customer(id=row[0], name=row[1], email=row[2])
        return None