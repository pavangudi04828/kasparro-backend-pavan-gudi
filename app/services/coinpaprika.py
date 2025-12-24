import requests
from datetime import datetime
from app.config import COINPAPRIKA_API_KEY
from app.utils.retry import retry

URL = "https://api.coinpaprika.com/v1/tickers"

def fetch_coinpaprika():
    headers = {}

    if COINPAPRIKA_API_KEY:
        headers["Authorization"] = f"Bearer {COINPAPRIKA_API_KEY}"

    def call():
        response = requests.get(URL, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()

    data = retry(call)
    results = []

    if not data:
        return results

    for coin in data[:5]:
        results.append({
            "source": "coinpaprika",
            "coin": coin["name"],
            "symbol": coin["symbol"],
            "price": coin["quotes"]["USD"]["price"],
            "market_cap": coin["quotes"]["USD"]["market_cap"],
            "timestamp": datetime.utcnow()
        })

    return results
