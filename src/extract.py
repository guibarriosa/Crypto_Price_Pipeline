import requests
import json
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

def extract():
    response = requests.get(URL, params=PARAMS)
    data = response.json()
    return data

def save_local(data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crypto_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(data, f)
    
    print(f"Saved: {filename}")

if __name__ == "__main__":
    data = extract()
    save_local(data)