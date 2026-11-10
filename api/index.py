from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "HortiLitoral API online"}

@app.get("/api/lotes")
def get_lotes():
    return [
        {"id": 1, "nome": "Tomate Longa Vida", "peso": 50.0, "validade": "2026-11-15"},
        {"id": 2, "nome": "Alface Crespa", "peso": 20.0, "validade": "2026-11-10"}
    ]