import requests

token=["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex"]

def get_tvl(token_input):
    url = "https://api.llama.fi/tvl/"+token_input
    response = requests.get(url)
    data = response.json()
    tvl = data
    return tvl

for x in range(7):
    print(token[x])
    print(round(get_tvl(token[x])/1000000,1))
    pass