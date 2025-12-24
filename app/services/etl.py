from app.database import SessionLocal, engine
from app.models import CryptoPrice, Base
from app.services.coingecko import fetch_coingecko
from app.services.coinpaprika import fetch_coinpaprika

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def run_etl():
    db = SessionLocal()

    data = []
    data.extend(fetch_coingecko())
    data.extend(fetch_coinpaprika())

    for item in data:
        db.add(CryptoPrice(**item))

    db.commit()
    db.close()

    return len(data)
