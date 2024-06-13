import sqlite3


def init_db():
    conn = sqlite3.connect("wallets.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS wallets
            (id INTEGER PRIMARY KEY,
            address TEXT NOT NULL,
            private_key TEXT NOT NULL)"""
    )
    conn.commit()
    conn.close()


def add_wallet(address, private_key):
    conn = sqlite3.connect("wallets.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO wallets (address, private_key) VALUES (?, ?)",
        (address, private_key),
    )
    conn.commit()
    conn.close()


def get_wallet(id):
    conn = sqlite3.connect("wallets.db")
    cursor = conn.cursor()
    res = cursor.execute(
        f"SELECT * FROM wallets WHERE id = {id}",
    )
    wallet_row = res.fetchone()
    conn.close()
    return wallet_row
