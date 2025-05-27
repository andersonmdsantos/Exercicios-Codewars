# Container

Essa branch foi criada para desenvolver habilidades de como usar o Docker.

# Para executar um script, você precisa ter:

- `Python 3.10 ou superior`
- `Docker 28.1.1 ou superior`

## Instalando as dependências
Recomenda-se utilizar um ambiente virtual para evitar conflitos com outras dependências.
Crie o ambiente virtual:
```
python -m venv container
```

Para ativar o ambiente, digite no CMD
```
container\Scripts\activate.bat
```

Para desativar o ambiente, digite no CMD
```
deactivate

ou 

container\Scripts\deactivate.bat
```

## Como Executar
1 - Após fazer o clone do repositório, navegue até a pasta do projeto:
```
1. cd /caminho/do/projeto
```
2 - Contruir a imagem docker
```
docker build -t hello-python .
```
Onde:
```
1. -t hello-python: dá um nome à imagem Docker
2. .: indica que o Dockerfile está no diretório atual
```

Depois de construir a imagem, rode o container:
```
docker run hello-python
```

O conteudo de app.py deve ser exibido, exemplo:
```
Olá, Docker + Python!
```

## (Opcional) Modo de desenvolvimento com volume
Se você quiser testar alterações no código sem precisar reconstruir a imagem toda vez, use volumes:
```
docker run -v "C:/caminho/do/projeto":/app -w /app python:3.11-slim python app.py
```

-v "C:/caminho/do/projeto":/app	- Monta sua pasta local no container na pasta /app

-w /app	- Define o diretório de trabalho dentro do container

python:3.11-slim python app.py - Usa a imagem do Python e executa o arquivo