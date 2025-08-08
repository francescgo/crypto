import requests
import numpy as np
import matplotlib.pyplot as plt


token=["velodrome","aerodrome","thena","ramses-exchange","equalizer","lynex","ocelex"]
MarketCap=[0,0,0,0,0,0,0]
Revenue=[0,0,0,0,0,0,0]
PER=[0,0,0,0,0,0,0]

def get_rev1yr(token_input):
    url = "https://api.llama.fi/summary/fees/"+token_input
    response = requests.get(url)
    data = response.json()
    rev7d = data["total7d"]
    if rev7d==None:
        return 0
        pass
    rev1yr=rev7d*52
    return rev1yr

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
    MarketCap[x]=round(get_mcap(token[x])/1000000,1)
    Revenue[x]=round(get_rev1yr(token[x])/1000000,3)
    pass

np_PER=np.array(PER)
np_MC=np.array(MarketCap)
np_REV=np.array(Revenue)
np_PER=np_MC/np_REV

for x in range(7):
    print(token[x])
    print(MarketCap[x])
    print(Revenue[x])
    print(np_PER[x])
    pass

plt.scatter(MarketCap,Revenue)
plt.show()