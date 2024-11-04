# Use uma imagem base do Python
FROM python:3.12-slim

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto
COPY . .

#
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
