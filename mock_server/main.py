import os
import json
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any

app = FastAPI(title="Ironman Mock API Server")

# Mock database (in-memory or from JSON files)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_mock_data(filename: str) -> List[Dict[str, Any]]:
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

@app.get("/")
async def root():
    return {"message": "Ironman Mock API Server is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

# --- OrangePet Mock Endpoints ---

@app.get("/products")
async def get_products():
    data = load_mock_data("products.json")
    return data

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    products = load_mock_data("products.json")
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/login")
async def login(credentials: Dict[str, str]):
    if credentials.get("username") == "admin" and credentials.get("password") == "password":
        return {"token": "mock-jwt-token-12345", "status": "success"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
