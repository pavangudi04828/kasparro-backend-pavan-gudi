from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    coin = Column(String)
    symbol = Column(String)
    price = Column(Float)
    market_cap = Column(Float)
    timestamp = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
