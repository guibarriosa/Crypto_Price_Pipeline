from extract import extract, get_symbols
from transform import transform
from conn import get_connection, initialize_db, close_connection
from load import save_to_s3, save_to_database

def handler(event, context):
    main()

def main():
    get_connection()
    
    raw_data = extract()
    processed_data = transform(raw_data)
    symbols = get_symbols()

    save_to_s3(raw_data, prefix="raw")
    save_to_s3(processed_data, prefix="processed")
    initialize_db()
    save_to_database(processed_data, symbols)
    
    close_connection()

if __name__ == "__main__":
    main()   
    