# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos locais para o container
COPY . /app

# Comando que roda o script Python
CMD ["python", "app.py"]