#!/bin/sh
# entrypoint.sh

# Esperar pelo banco de dados PostgreSQL estar disponível
while ! nc -z postgres-service 5432; do
  echo "Aguardando o PostgreSQL iniciar..."
  sleep 1
done

echo "PostgreSQL está disponível. Iniciando a aplicação..."

# Executar migrações e iniciar o servidor
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
