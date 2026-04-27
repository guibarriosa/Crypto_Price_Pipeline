import conn as db


def create_crypto(name, symbol, currency):
    db.cursor.execute("INSERT INTO crypto (name, symbol, currency) " \
    "VALUES (%s, %s, %s)", (name, symbol, currency))
    db.conn.commit()
    return db.cursor.lastrowid

def show_cryptos():
    db.cursor.execute("select * from crypto")
    for row in db.cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Symbol: {row[2]}, Currency: {row[3]}")

def show_prices():
    db.cursor.execute("select * from prices")
    for row in db.cursor.fetchall():
        print(f"ID: {row[0]}, Crypto ID: {row[1]}, Price: {row[2]}, Date: {row[3]}")

def delete_tables():
    db.cursor.execute("DROP TABLE IF EXISTS prices")
    db.cursor.execute("DROP TABLE IF EXISTS crypto")
    db.conn.commit()
    print("Tables deleted successfully!")

