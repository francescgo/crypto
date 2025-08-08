import requests
import time

token=["velodrome-finance","aerodrome-finance","thena","ramses-exchange","equalizer-on-sonic","lynex"]

def get_fully_diluted_value(token_input):
    url = "https://api.coingecko.com/api/v3/coins/"+token_input
    response = requests.get(url)
    data = response.json()
    fully_diluted_value = data["market_data"]["fully_diluted_valuation"]["usd"]
    return fully_diluted_value

for x in range(6):
    print(token[x])
    print(round(get_fully_diluted_value(token[x])/1000000,1))
    time.sleep(5)
    pass
