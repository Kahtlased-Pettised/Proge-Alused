import requests

parameetrid = {
    }

url = "https://randomfox.ca/floof/?ref=apilist.fun"

päring = requests.get(url, params=parameetrid)
andmed =  päring.json()
pilt = andmed["link"]
print(pilt)