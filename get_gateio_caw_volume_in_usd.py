import requests

def get_gateio_caw_volume_in_usd():
    """
    Fetches the 24-hour trading volume of CAW from Gate.io and calculates its USD equivalent.
    
    Returns:
        float: 24-hour trading volume of CAW in USD.
    """
    url = "https://api.gateio.ws/api/v4/spot/tickers"
    params = {"currency_pair": "CAW_USDT"}  
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            caw_volume = float(data[0].get("base_volume", 0))  # CAW traded in 24h
            caw_price = float(data[0].get("last", 0))  # Latest CAW price in USDT
            return caw_volume * caw_price  # Convert to USD
        else:
            print("Error: No data found for CAW.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return None
