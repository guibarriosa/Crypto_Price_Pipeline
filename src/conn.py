import os
import pymysql

# If you want to test locally, uncomment the following lines and create a .env file 
# with your database credentials
'''from dotenv import load_dotenv
load_dotenv()'''

conn = None
cursor = None 

# Here we establish a connection to the RDS MySQL database using environment variables 
# and returns the connection and cursor.
def get_connection():
    global conn, cursor
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_disabled=True,
    )
    cursor = conn.cursor()
    return conn, cursor

# Here we create the necessary tables in the database if they don't already exist. 
def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        symbol VARCHAR(10) NOT NULL,
        currency VARCHAR(10) NOT NULL,
        UNIQUE KEY unique_symbol_currency (symbol, currency)
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

def close_connection():
    cursor.close()
    conn.close() 