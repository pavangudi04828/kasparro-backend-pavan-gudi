from fastapi import APIRouter
from app.services.etl import run_etl
from app.database import SessionLocal
from app.models import CryptoPrice

router = APIRouter()

@router.post("/etl/run")
def run():
    count = run_etl()
    return {"inserted_records": count}

@router.get("/prices/latest")
def latest():
    db = SessionLocal()
    data = (
        db.query(CryptoPrice)
        .order_by(CryptoPrice.created_at.desc())
        .limit(10)
        .all()
    )
    db.close()
    return data
