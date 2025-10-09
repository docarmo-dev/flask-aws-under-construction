# Flask + MongoDB Atlas + Frontend (Under Construction) 🚧

Este projeto separa **backend** (Flask + MongoDB Atlas) e **frontend** (HTML + CSS com Jinja2).

## Estrutura
```
flask_mongo_template/
├── backend/
│   ├── app.py
│   ├── .env.example
│   └── requirements.txt
└── frontend/
    ├── templates/
    │   └── index.html
    └── static/
        └── css/style.css
```

## Configuração local
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edite .env e adicione sua MONGO_URI do Atlas
python app.py
```

O servidor rodará em http://0.0.0.0:80

## Rotas disponíveis
| Método | Rota | Descrição |
|---------|------|------------|
| GET | / | Página inicial |
| GET | /api/users | Lista todos os usuários |
| POST | /api/users | Adiciona novo usuário (JSON: name, email) |
| DELETE | /api/users/<name> | Remove usuário por nome |
