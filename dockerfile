# Usar uma imagem base do Python 3.11
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y netcat-openbsd gcc

# Copiar arquivos de requisitos
COPY pyproject.toml poetry.lock ./

# Instalar o Poetry
RUN pip install poetry

# Instalar as dependências
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copiar o restante do código
COPY . .

# Expor a porta 8000
EXPOSE 8000

# Copiar o script de entrada
COPY infrastructure/kubernetes/entrypoint.sh .

# Tornar o script executável
RUN chmod +x entrypoint.sh

# Definir o entrypoint
ENTRYPOINT ["./entrypoint.sh"]
