# Machine Learning

Essa branch foi criada para desenvolver habilidades de como usar Machine Learning com Python

# Para executar um script, você precisa ter:

- `Python 3.10 ou superior`
- `Pandas 2.2.3 ou superior`
- `Scikit-learn 1.6.1 ou superior`
- `Streamlit 1.45 ou superior`
- `Matplotlib 3.10.3 ou superior`
- `Jupyterlab 4.4.3 ou superior`

## Instalando as dependências
Recomenda-se utilizar um ambiente virtual para evitar conflitos com outras dependências.
Crie o ambiente virtual:
```
python -m venv machine-learning
```

Para ativar o ambiente, digite no CMD
```
machine-learning\Scripts\activate.bat
```

Para desativar o ambiente, digite no CMD
```
deactivate

ou 

machine-learning\Scripts\deactivate.bat
```

## Instalando as bibliotecas

```
pip install pandas scikit-learn streamlit matplotlib jupyterlab
```

## Como Executar
1 - Após fazer o clone do repositório, navegue até a pasta do projeto:
```
cd /caminho/do/projeto/
```
2 - Rode a aplicação
```
streamlit run app.py
```
Esse comando irá mostrar sua aplicação web em funcionamento

Para encerrar, basta pressionar Ctrl + C no terminal

Caso tenha tentado rodar a aplicação e reportou a mensagem
```
'streamlit' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.
```

Verifique se o comando pip reconhece suas libs instaladas usando 'pip list'

Se voltar somente python 3.x quer dizer que o ambiente virtual está desativado, então basta ativa-lo novamente