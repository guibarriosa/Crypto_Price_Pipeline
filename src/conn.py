import mysql.connector
import os

'''from dotenv import load_dotenv
load_dotenv()'''

conn = None
cursor = None

def get_connection():
    global conn, cursor
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_ca="global-bundle.pem"
    )
    cursor = conn.cursor()
    return conn, cursor

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
        price DECIMAL(12, 6) NOT NULL,
        date DATETIME NOT NULL,
        FOREIGN KEY (crypto_id) REFERENCES crypto(id)
    )
    """)
    conn.commit()
    print("Tables created successfully!")

def conn_close():
    cursor.close()
    conn.close() 