from datetime import datetime
from extract import PARAMS 
# Here we take the raw data from the API and transform it into a list of dictionaries for easier handling.
def transform(data):
    transformed_data = []

    for coin, values in data.items():
        transformed_data.append({
            "coin": coin.capitalize(),
            "price": values[PARAMS["vs_currencies"]],
        })

    return transformed_data