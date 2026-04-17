import boto3
import json
from datetime import datetime
from conn import conn, cursor

BUCKET_NAME = "crypto-pipeline-gui"

def save_to_s3(data, prefix):
    s3 = boto3.client("s3")

    timestamp = datetime.now().strftime("%HH-%MM-%SS")
    key = f"{prefix}/Year={datetime.now().year}/Month={datetime.now().month}/Day={datetime.now().day}/crypto_{timestamp}.json"

    json_data = json.dumps(data)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json_data,
        ContentType="application/json"
    )

def save_to_database(json_data: list, symbols: dict):
    
    inserted = 0
    skipped = 0

    for coin_name in symbols.keys():
        cursor.execute("INSERT IGNORE INTO crypto (name, symbol, currency) VALUES (%s, %s, %s)",
        (coin_name, symbols[coin_name], "EUR"))

        print(f"Crypto '{coin_name}' inserida ou já existe na tabela.")
    
    for entry in json_data:
        coin_name = entry["coin"]
        price = round(entry["price_eur"], 6)
        date = datetime.now().replace(microsecond=0)  

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
        print(f"Preço de '{coin_name}' inserido com sucesso: {price} EUR em {date}.")
    
    conn.commit()
    
    print(f"[OK] {inserted} preços inseridos, {skipped} ignorados.")

