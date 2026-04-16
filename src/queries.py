from datetime import datetime
from conn import conn

cursor = conn.cursor()

def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        symbol VARCHAR(10) NOT NULL UNIQUE,
        currency VARCHAR(10) NOT NULL
    )
    """)

    cursor.execute("""                                 
    CREATE TABLE IF NOT EXISTS prices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        crypto_id INT NOT NULL,
        price DECIMAL(18, 8) NOT NULL,
        date DATETIME NOT NULL,
        FOREIGN KEY (crypto_id) REFERENCES crypto(id)
    )
    """)
    conn.commit()
    print("Tables created successfully!")

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

def save_to_database(json_data: list, symbols: dict):
    
    inserted = 0
    skipped = 0

    for coin_name in symbols.keys():
        cursor.execute("INSERT IGNORE INTO crypto (name, symbol, currency) VALUES (%s, %s, %s)",
        (coin_name, symbols[coin_name], "EUR"))

        print(f"Crypto '{coin_name}' inserida ou já existe na tabela.")
    
    for entry in json_data:
        coin_name = entry["coin"]
        price = entry["price_eur"]

        time_parts = entry["timestamp"].replace("H", "").replace("M", "").replace("S", "").split("-")
        hour, minute, second = int(time_parts[0]), int(time_parts[1]), int(time_parts[2])
        date = datetime.now().replace(hour=hour, minute=minute, second=second, microsecond=0)
        
        cursor.execute("SELECT id FROM crypto WHERE name = %s", (coin_name,))
        result = cursor.fetchone()
        
        if result is None:
            print(f"['{coin_name}' não se encontra na tabela.")
            skipped += 1
            continue
        
        crypto_id = result[0]
        
        cursor.execute(
            "INSERT INTO prices (crypto_id, price, date) VALUES (%s, %s, %s)",
            (crypto_id, price, date)
        )
        inserted += 1
    
    conn.commit()
    
    print(f"[OK] {inserted} preços inseridos, {skipped} ignorados.")