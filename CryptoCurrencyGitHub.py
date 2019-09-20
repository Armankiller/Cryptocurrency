import requests
import sys
currency_name = sys.argv[1]
response = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{currency_name}/').json()
print(f'${response[0]["price_usd"]}')