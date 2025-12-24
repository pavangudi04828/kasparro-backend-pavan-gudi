from pydantic import BaseModel
from datetime import datetime

class CryptoOut(BaseModel):
    source: str
    coin: str
    symbol: str
    price: float
    market_cap: float
    timestamp: datetime
