import requests
from config import API_KEY_CMC

def get_cmc_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=CAW,CRO"
    headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY_CMC}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return {
            "price_caw": data["data"]["CAW"]["quote"]["USD"]["price"],
            "market_cap_caw": data["data"]["CAW"]["quote"]["USD"]["market_cap"],
            "volume_24h_caw": data["data"]["CAW"]["quote"]["USD"]["volume_24h"],
            "price_cro": data["data"]["CRO"]["quote"]["USD"]["price"],
            "market_cap_cro": data["data"]["CRO"]["quote"]["USD"]["market_cap"],
            "volume_24h_cro": data["data"]["CRO"]["quote"]["USD"]["volume_24h"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CMC data: {e}")
        return None
