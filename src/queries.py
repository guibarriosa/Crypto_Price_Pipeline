from datetime import datetime
from conn import conn

cursor = conn.cursor()

def create_crypto(name, symbol, currency):
    cursor.execute("INSERT INTO crypto (name, symbol, currency) " \
    "VALUES (%s, %s, %s)", (name, symbol, currency))
    conn.commit()
    return cursor.lastrowid

def show_cryptos():
    cursor.execute("select * from crypto")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Symbol: {row[2]}, Currency: {row[3]}")

def show_prices():
    cursor.execute("select * from prices")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Crypto ID: {row[1]}, Price: {row[2]}, Date: {row[3]}")

def delete_tables():
    cursor.execute("DROP TABLE IF EXISTS prices")
    cursor.execute("DROP TABLE IF EXISTS crypto")
    conn.commit()
    print("Tables deleted successfully!")

