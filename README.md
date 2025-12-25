# Kasparro Backend Assignment – Crypto ETL System

## Overview
This project is a production-style backend system that demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for cryptocurrency market data.

The system fetches data from multiple external APIs, normalizes it into a common format, stores it in a database, and exposes REST APIs to trigger the ETL pipeline and retrieve processed data.
---

## Architecture

The backend follows a clean ETL-based architecture:

1. **Extract**
   - Fetches cryptocurrency market data from external APIs:
     - CoinGecko API
     - CoinPaprika API

2. **Transform**
   - Converts different API responses into a single normalized schema
   - Ensures consistent fields such as coin name, symbol, price, market cap, and timestamp

3. **Load**
   - Stores transformed data into a relational database using SQLAlchemy

4. **Serve**
   - Exposes REST APIs using FastAPI
   - Allows triggering ETL and fetching stored data
---

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **HTTP Client:** Requests
- **API Documentation:** Swagger (OpenAPI)
- **Environment Management:** python-dotenv
---

## Project Structure

```
kasparro-backend-pavan-gudi/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services/
│   │   ├── coingecko.py
│   │   ├── coinpaprika.py
│   │   └── etl.py
│   ├── routes/
│   │   └── crypto.py
│   └── utils/
│       └── retry.py
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## API Endpoints

### POST `/etl/run`
Triggers the ETL pipeline.  
Fetches data from CoinGecko and CoinPaprika, normalizes it, and stores it in the database.

**Response Example**
```json
{
  "inserted_records": 10
}


---

### GET `/prices/latest`
Returns the most recent cryptocurrency records stored in the database.

**Response Example**
```json
[
  {
    "source": "coingecko",
    "coin": "Bitcoin",
    "symbol": "btc",
    "price": 87032,
    "market_cap": 1738332448120,
    "timestamp": "2025-12-24T16:17:37.405393"
  }
]
---

## Error Handling & Reliability

- Automatic retry mechanism for external API failures
- Graceful handling of network timeouts
- Prevents server crashes due to API unavailability
- Clean database session handling

---

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Start the server
```
uvicorn app.main:app --reload
```

### 3. Open Swagger UI
```
http://127.0.0.1:8000/docs
```


## Author
Pavan Gudi

