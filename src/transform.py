from datetime import datetime

def transform(data):
    transformed_data = []

    for coin, values in data.items():
        transformed_data.append({
            "coin": coin,
            "price_eur": values["eur"],
        })

    return transformed_data