import requests
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum,cardano,solana",
    "vs_currencies": "eur"
}

def extract():
    response = requests.get(URL, params=PARAMS)
    data = response.json()  
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")       
   
    return data

