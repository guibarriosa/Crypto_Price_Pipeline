from extract import extract
from tranform import transform
from load import save_to_s3


def main():
    raw_data = extract()
    processed_data = transform(raw_data)

    save_to_s3(raw_data, prefix="raw")
    save_to_s3(processed_data, prefix="processed")

if __name__ == "__main__":
    main()    