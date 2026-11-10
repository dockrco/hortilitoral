from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="HortiLitoral PWA")

# Se os seus arquivos estáticos (CSS, JS, imagens) estiverem numa pasta chamada "static" ou "public":
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    # Caminho para o seu index.html real
    return FileResponse("index.html") # ou "public/index.html" dependendo de onde ele está

@app.get("/api/lotes")
def get_lotes():
    return [
        {"id": 1, "nome": "Tomate Longa Vida", "peso": 50.0, "validade": "2026-11-15"},
        {"id": 2, "nome": "Alface Crespa", "peso": 20.0, "validade": "2026-11-10"}
    ]