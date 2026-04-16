import mysql.connector

password = "barriosa123"

conn = mysql.connector.connect(
    host="rds-crypto-db.c4bm6c2eep8m.us-east-1.rds.amazonaws.com",
    user="gui",
    password=password,
    database="crypto_db",
    ssl_ca="./global-bundle.pem"
)

if conn.is_connected():
    print("Connection to RDS MySQL database was successful!")