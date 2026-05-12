import requests

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum,cardano,solana",  # Specify the coins you want to track here, separated by commas
    "vs_currencies": "eur"                     # Specify the currency you want the prices in (e.g., "eur" for Euro, "usd" for US Dollar)
}

# This function is responsible for making the API request to CoinGecko and returning the data as a JSON object. 
# It also checks if the request was successful and raises an exception if it wasn't.
def extract():
    response = requests.get(URL, params=PARAMS)
    data = response.json()  
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")       

    return data

# This function retrieves the list of all cryptocurrencies from the CoinGecko API 
# and filters it to return only the symbols for the specified coins.
def get_symbols():
    response = requests.get("https://api.coingecko.com/api/v3/coins/list")
    all_coins = response.json()
    symbols = {}

    for coin in all_coins:
        if coin["id"] in PARAMS["ids"].split(","):
            symbols[coin["id"].capitalize()] = coin["symbol"].upper()
            
    symbols_sorted= dict(sorted(symbols.items()))
    return symbols_sorted