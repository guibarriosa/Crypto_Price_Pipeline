from extract import *
from transform import transform
from conn import initialize_db, conn_close
from load import save_to_s3, save_to_database
from queries import *

def handler(event, context):
    main()

def main():
    raw_data = extract()
    processed_data = transform(raw_data)
    symbols = get_symbols()

    save_to_s3(raw_data, prefix="raw")
    save_to_s3(processed_data, prefix="processed")
    initialize_db()
    save_to_database(processed_data, symbols)
    #show_prices()
    conn_close()
    #show_cryptos()
    #show_prices()
    #delete_tables()

if __name__ == "__main__":
    main()   
    