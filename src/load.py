import boto3
import json
from datetime import datetime
import conn as db   
from extract import PARAMS

BUCKET_NAME = "crypto-pipeline-gui" # Insert your bucket name here

s3 = boto3.client("s3")

def save_to_s3(data, prefix):

    timestamp = datetime.now().strftime("%HH-%MM-%SS")
    key = f"{prefix}/Year={datetime.now().year}/Month={datetime.now().month}/Day={datetime.now().day}/crypto_{timestamp}.json"

    json_data = json.dumps(data)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json_data,
        ContentType="application/json"
    )

def save_to_database(data: list, symbols: dict):
    
    inserted = 0
    
    # Create crypto entries first, then insert prices. This way we avoid foreign key constraint errors 
    # and ensure all cryptos are present in the crypto table before inserting prices.
    for coin_name in symbols.keys():
        db.cursor.execute(
            "INSERT IGNORE INTO crypto (name, symbol, currency) VALUES (%s, %s, %s)",
            (coin_name, symbols[coin_name], PARAMS["vs_currencies"].upper())
        )

        if db.cursor.rowcount == 1:
            print(f"'{coin_name}' in '{PARAMS['vs_currencies'].upper()}' inserted into the table.")
        else:
            print(f"'{coin_name}' in '{PARAMS['vs_currencies'].upper()}' already exists in the table.")
    
    for entry in data:
        coin_name = entry["coin"]
        price = round(entry["price"], 6)
        # Remove microseconds, we dont need that level of precision for our use case 
        # and it can cause issues with MySQL datetime format
        date = datetime.now().replace(microsecond=0)  

        db.cursor.execute(
            "SELECT id FROM crypto WHERE name = %s AND currency = %s", 
            (coin_name, PARAMS["vs_currencies"].upper())
        )
        result = db.cursor.fetchone()
        crypto_id = result[0]

        print(f"Price for '{coin_name}' in '{PARAMS['vs_currencies'].upper()}' inserted: {price}.")
        db.cursor.execute(
            "INSERT INTO prices (crypto_id, price, date) VALUES (%s, %s, %s)", 
            (crypto_id, price, date)
        )
        inserted += 1

    db.conn.commit()
    
    print(f"{inserted} prices inserted.")

