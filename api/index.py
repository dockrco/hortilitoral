from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="HortiLitoral PWA")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HortiLitoral PWA - Gestão de Hortifrúti</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
            .container { background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); max-width: 600px; width: 100%; border: 1px solid #334155; }
            .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
            h1 { font-size: 22px; margin: 0; color: #38bdf8; }
            .badge { background: #065f46; color: #34d399; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }
            .card { background: #0f172a; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #38bdf8; }
            .card h3 { margin: 0 0 5px 0; font-size: 16px; color: #e2e8f0; }
            .card p { margin: 0; font-size: 14px; color: #94a3b8; }
            .footer { margin-top: 20px; text-align: center; font-size: 12px; color: #64748b; }
            a { color: #38bdf8; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🥬 HortiLitoral PWA</h1>
                <span class="badge">● Online (Vercel)</span>
            </div>
            <p style="color: #94a3b8; margin-bottom: 20px;">Sistema de Gestão de Lotes FIFO e Alertas de Validade para Distribuidores.</p>
            
            <div class="card">
                <h3>Lote #01 - Tomate Longa Vida</h3>
                <p>Peso: 50.0 kg | Validade: 2026-11-15 | Status: <span style="color: #34d399;">Ativo (FIFO)</span></p>
            </div>
            
            <div class="card">
                <h3>Lote #02 - Alface Crespa</h3>
                <p>Peso: 20.0 kg | Validade: 2026-11-10 | Status: <span style="color: #f87171;">Atenção (Próx. Vencimento)</span></p>
            </div>

            <div class="footer">
                Documentação da API / Endpoints: <a href="/docs" target="_blank">/docs (Swagger UI)</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/api/lotes")
def get_lotes():
    return [
        {"id": 1, "nome": "Tomate Longa Vida", "peso": 50.0, "validade": "2026-11-15"},
        {"id": 2, "nome": "Alface Crespa", "peso": 20.0, "validade": "2026-11-10"}
    ]