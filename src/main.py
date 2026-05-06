from extract import extract, get_symbols
from transform import transform
from conn import get_connection, initialize_db, conn_close
from load import save_to_s3, save_to_database
from queries import *

def handler(event, context):
    main()

def main():
    print("1. A iniciar conexão ao RDS...")
    get_connection()
    
    print("2. A extrair dados da API...")
    raw_data = extract()
    print("3. A processar dados...")
    processed_data = transform(raw_data)
    print("4. A obter símbolos...")
    symbols = get_symbols()

    print("5. A guardar dados no S3...")
    save_to_s3(raw_data, prefix="raw")
    save_to_s3(processed_data, prefix="processed")
    print("6. A inicializar a base de dados...")
    initialize_db()
    print("7. A guardar dados na RDS...")
    save_to_database(processed_data, symbols)
    #show_prices()
    print("8. A fechar conexão ao RDS...")
    conn_close()
    #show_cryptos()
    #show_prices()
    #delete_tables()

if __name__ == "__main__":
    main()   
    