import requests

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

def get_symbols():
    response = requests.get("https://api.coingecko.com/api/v3/coins/list")
    all_coins = response.json()
    symbols = {}

    coins = ["bitcoin", "ethereum", "cardano", "solana"]
    for coin in all_coins:
        if coin["id"] in coins:
            symbols[coin["id"]] = coin["symbol"].upper()
            
    symbols_sorted= dict(sorted(symbols.items()))
    return symbols_sorted