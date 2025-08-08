import requests
import time
import pandas as pd

token_gecko = ["velodrome-finance","aerodrome-finance","thena","ramses-exchange","equalizer-on-sonic","lynex","ocelex","catex"]
token_llama = ["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex","catex"]
token = ["velodrome","aerodrome","thena","ramses","equalizer","lynex","ocelex","catex"]
result = { }

headers = {'User-Agent': 'Mozilla/5.0'}

#Getting Fully Diluted Value from Coingecko
def get_fully_diluted_value(token_input):
    url = "https://api.coingecko.com/api/v3/coins/"+token_input
    try:
        response = requests.get(url)
        data = response.json()
        # Verifica si existe la clave 'market_data' y lo necesario dentro
        if (
            'market_data' in data and
            'fully_diluted_valuation' in data['market_data'] and
            'usd' in data['market_data']['fully_diluted_valuation']
            ):
                fdv = data["market_data"]["fully_diluted_valuation"]["usd"]
                return round(fdv / 1_000_000, 1)  # FDV en millones de USD
        else:
            print(f"[ADVERTENCIA] Faltan datos de FDV para '{token_input}'")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Fallo en la solicitud para '{token_input}': {e}")
        return 0
    except Exception as e:
        print(f"[ERROR] Error inesperado para '{token_input}': {e}")
        return 0
    
#Getting Total Value Locked from Defi Llama
def get_tvl(token_input):
    url = f"https://api.llama.fi/tvl/"+token_input
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return round(data / 1_000_000, 1) if isinstance(data, (int, float)) else 0
    except Exception as e:
        print(f"Error fetching TVL for {token_input}: {e}")
        return 0

#Getting 7d Revenue from Defi Llama
def get_rev7d(token_input):
    url = f"https://api.llama.fi/summary/fees/{token_input}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        rev7d = data.get("total7d", 0)
        return round(rev7d / 1_000_000, 3) if rev7d else 0
    except Exception as e:
        print(f"Error fetching 7d revenue for {token_input}: {e}")
        return 0


#Getting Market Cap from Defi Llama
def get_mcap(token_input):
    url = f"https://api.llama.fi/protocol/{token_input}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        mcap = data.get("mcap", 0)
        return round(mcap / 1_000_000, 1) if mcap else 0
    except Exception as e:
        print(f"Error fetching market cap for {token_input}: {e}")
        return 0


for x in range(7):
    result[token[x]] = {}
    if x<6:
        fdv = get_fully_diluted_value(token_gecko[x])
        if fdv is not None:
            result[token[x]]['fdv'] = fdv
    else: result[token[x]]['fdv'] = 0
    result[token[x]]['tvl'] = get_tvl(token_llama[x])
    if x<6: result[token[x]]['rev7d'] = get_rev7d(token_llama[x])
    else: result[token[x]]['rev7d'] = 0
    result[token[x]]['mcap'] = get_mcap(token_llama[x])
    time.sleep(5)
    if result[token[x]]['rev7d'] != 0 :
        result[token[x]]['per'] = result[token[x]]['mcap']/result[token[x]]['rev7d']/52
        result[token[x]]['fdper'] = result[token[x]]['fdv']/result[token[x]]['rev7d']/52
        pass
    else:
        result[token[x]]['per'] = 'N/A'
        result[token[x]]['fdper'] = 'N/A'
    pass

solidly=pd.DataFrame(result)

print(solidly)

solidly.to_csv("solidly.csv")
