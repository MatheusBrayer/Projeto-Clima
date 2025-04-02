import os

import requests
from datetime import datetime
import pytz
import sqlite3
from dotenv import load_dotenv

load_dotenv('chave_api.env')

api_key = os.getenv('CHAVE_API')

if api_key:
    print('Chave carregada com sucesso!')
else:
    print('Chave API não encontrada!')

# URL da API OpenWeatherMap para a cidade de Parobé
url = f"https://api.openweathermap.org/data/2.5/weather?q=Parobé&appid={api_key}&units=metric&lang=pt_br"

# Fazendo a requisição para a API
resposta = requests.get(url)

# Verificando se a resposta foi bem-sucedida (código 200)
if resposta.status_code == 200:
    dados = resposta.json()

    # Extraindo informações
    cidade = dados["name"]
    descricao = dados["weather"][0]["description"]
    temperatura = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    umidade = dados["main"]["humidity"]
    pressao = dados["main"]["pressure"]
    vento = dados["wind"]["speed"]
    latitude = dados["coord"]["lat"]
    longitude = dados["coord"]["lon"]

    # Convertendo o horário do nascer e pôr do sol usando timezone-aware datetime
    utc_zone = pytz.utc
    brt_zone = pytz.timezone('America/Sao_Paulo')

    nascer_do_sol_utc = datetime.fromtimestamp(dados["sys"]["sunrise"], utc_zone)
    por_do_sol_utc = datetime.fromtimestamp(dados["sys"]["sunset"], utc_zone)

    # Convertendo para o horário de Brasília (UTC-3)
    nascer_do_sol_brt = nascer_do_sol_utc.astimezone(brt_zone).strftime('%H:%M:%S')
    por_do_sol_brt = por_do_sol_utc.astimezone(brt_zone).strftime('%H:%M:%S')

    # Criar conexão com SQLite e banco de dados clima.db
    conexao = sqlite3.connect("clima.db")
    cursor = conexao.cursor()

    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clima (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT,
            descricao TEXT,
            temperatura REAL,
            sensacao REAL,
            umidade INTEGER,
            pressao INTEGER,
            vento REAL,
            nascer_do_sol TEXT,
            por_do_sol TEXT,
            data_coleta DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conexao.commit()
    conexao.close()

    # Conectar ao banco e inserir os dados
    conexao = sqlite3.connect("clima.db")
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO clima (cidade, descricao, temperatura, sensacao, umidade, pressao, vento, nascer_do_sol, por_do_sol)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cidade, descricao, temperatura, sensacao, umidade, pressao, vento, nascer_do_sol_brt, por_do_sol_brt))

    # Salvar alterações e fechar conexão
    conexao.commit()
    conexao.close()

    print("Dados salvos no banco de dados com sucesso!")


else:
    print("Erro ao obter dados da API. Código de erro:", resposta.status_code)
