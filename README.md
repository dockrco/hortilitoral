# HortiLitoral PWA - MVP de Gestão Logística e FIFO

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal.svg)](https://fastapi.tiangolo.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38BDF8.svg)](https://tailwindcss.com/)
[![PWA Ready](https://img.shields.io/badge/PWA-Installable-success.svg)](https://web.dev/progressive-web-apps/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Protótipo de Aplicativo Web Progressivo (PWA) real desenvolvido para a distribuidora de hortifrúti **HortiLitoral**, localizada em **Mongaguá, SP**. O projeto resolve os principais gargalos operacionais no chão de galpão: o controle inadequado de perecíveis (perdas por vencimento) e a fragmentação dos pedidos via WhatsApp.

---

## 🚀 Principais Funcionalidades & Arquitetura PWA

1. **Manifesto PWA (`manifest.json`):** Permite que o aplicativo seja instalado diretamente na tela inicial de dispositivos móveis ou desktops.
2. **Service Worker (`sw.js`):** Gerencia cache e suporte offline para garantir resiliência operacional no galpão.
3. **Autenticação Segura (Tela 1):** Simulação de login com hash Argon2 e emissão de Token JWT.
4. **Controle de Estoque & FIFO Estrito (Tela 2):** Cadastro de lotes com validação (Pydantic) e ordenação cronológica automática baseada no critério *First In, First Out* (FIFO).
5. **Centralização de Pedidos do WhatsApp & Picking (Tela 2):** Painel para centralizar pedidos e executar a baixa automática de estoque proporcional no lote mais antigo.
6. **Painel de Alertas Críticos e Resultados (Tela 3):** Alertas visuais/textuais para lotes com vencimento inferior a 48h (suporte ao ODS 12), histórico e métricas de acessibilidade mobile ($\ge$ 44x44px).

---

## 📂 Estrutura do Repositório

```text
hortilitoral-pwa/
├── index.html              # Protótipo PWA unificado com registro de SW
├── manifest.json           # Manifesto de Aplicativo Web Progressivo
├── sw.js                   # Service Worker para cache e suporte offline
├── backend/
    └── main.py             # API FastAPI com rotas e validação Pydantic
├── requirements.txt        # Dependências Python do backend
└── README.md               # Documentação oficial
```

---

## ⚙️ Como Executar

### 1. Executar o Front-end PWA
Basta abrir o arquivo `index.html` em um navegador web moderno (compatível com instalação PWA).

### 2. Executar o Back-end (FastAPI)
```bash
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload
```

---

## 📄 Licença
Esse projeto foi feito apenas para uso educacional e privado, protegido e distribuido sob a licença MIT. Veja `LICENSE` para mais informações.
