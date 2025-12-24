import requests
from datetime import datetime
from app.utils.retry import retry

URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_coingecko():
    def call():
        response = requests.get(
            URL,
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 5,
                "page": 1
            },
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    data = retry(call)
    results = []

    if not data:
        return results

    for coin in data:
        results.append({
            "source": "coingecko",
            "coin": coin["name"],
            "symbol": coin["symbol"],
            "price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "timestamp": datetime.utcnow()
        })

    return results

