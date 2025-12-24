from fastapi import FastAPI
from app.routes.crypto import router

app = FastAPI(title="Kasparro Backend Assignment")

app.include_router(router)
