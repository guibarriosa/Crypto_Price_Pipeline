from datetime import datetime

def transform(data):
    transformed_data = []
    timestamp = datetime.now().strftime("%HH-%MM-%SS")

    for coin, values in data.items():
        transformed_data.append({
            "coin": coin,
            "price_eur": values["eur"],
            "timestamp": timestamp
        })

    return transformed_data