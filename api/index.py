from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="HortiLitoral PWA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Lote(BaseModel):
    nome: str
    peso: float
    validade: str

# Base simulada para o MVP rodar liso no ambiente serverless
lotes_db = [
    {"id": 1, "nome": "Tomate Longa Vida", "peso": 50.0, "validade": "2026-11-12"},
    {"id": 2, "nome": "Alface Crespa", "peso": 20.0, "validade": "2026-11-10"}
]

@app.get("/")
def read_root():
    return {"status": "online", "project": "HortiLitoral PWA API"}

@app.get("/api/lotes")
def get_lotes():
    sorted_lotes = sorted(lotes_db, key=lambda x: x["validade"])
    return sorted_lotes

@app.post("/api/lotes")
def create_lote(lote: Lote):
    novo_lote = {
        "id": len(lotes_db) + 1,
        "nome": lote.nome,
        "peso": lote.peso,
        "validade": lote.validade
    }
    lotes_db.append(novo_lote)
    return {"message": "Lote cadastrado com sucesso!", "lote": novo_lote}

@app.get("/api/alertas")
def get_alertas():
    return lotes_db

@app.post("/api/pedidos-whatsapp")
def criar_pedido():
    return {"status": "sucesso", "mensagem": "Link do WhatsApp gerado com sucesso!"}