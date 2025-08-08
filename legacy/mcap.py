import requests

token=["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex"]

def get_mcap(token_input):
    url = "https://api.llama.fi/protocol/"+token_input
    response = requests.get(url)
    data = response.json()
    mcap = data["mcap"]
    if mcap==None:
        return 0
        pass
    return mcap

for x in range(7):
    print(token[x])
    print(round(get_mcap(token[x])/1000000,1))
    pass
