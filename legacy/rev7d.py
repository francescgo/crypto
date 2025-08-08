import requests

token = ["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex"]
result = {}

def get_rev7d(token_input):
    url = "https://api.llama.fi/summary/fees/"+token_input
    response = requests.get(url)
    data = response.json()
    rev7d = round(data["total7d"]/1000000,3)
    return rev7d


for x in range(7):
    result[token[x]] = get_rev7d(token[x])
    pass

print(result)
