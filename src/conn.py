import mysql.connector
import os

'''from dotenv import load_dotenv
load_dotenv()'''

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")  
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

print(os.getenv("DB_HOST"))

conn = mysql.connector.connect(
    host= DB_HOST,
    user= DB_USER,
    password= DB_PASSWORD,
    database= DB_NAME,
    ssl_ca="./global-bundle.pem"
)

print(os.getenv("DB_HOST"))

if conn.is_connected():
    print("Connection to RDS MySQL database was successful!")

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