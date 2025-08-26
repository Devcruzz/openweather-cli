import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Resgatando a chave da api do openweather
load_dotenv()
api_key = os.getenv("API_KEY")


# city_name = "fortaleza"

#FUNÇÃO QUE OBTEM OS DADOS VINDO DA API OPENWEATHER
def get_weather_from_api(api_key, city_name):
    try:
        base_url = "https://api.openweathermap.org/data/2.5/weather?units=metric&lang=pt_br&"
        #MODIFICANDO A URL PARA PASSAR OS DEMAIS PARÂMETROS
        url_modified = f"{base_url}appid={api_key}&q={city_name}"
        response = requests.get(url_modified)
    
       # verifica se a resposta foi bem sucedida
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            return {"erro": "API Key inválida ou não fornecida."}
        elif response.status_code == 404:
            return {"erro": f"Cidade '{city_name}' não encontrada."}
        elif response.status_code == 429:
            return {"erro": "Muitas requisições. Tente novamente mais tarde."}
        else:
            return {"erro": f"Erro inesperado: {response.status_code}"}

    except requests.exceptions.Timeout:
        return {"erro": "A requisição demorou muito (timeout)."}
    except requests.exceptions.ConnectionError:
        return {"erro": "Falha de conexão. Verifique sua internet."}
    except Exception as e:
        return {"erro": f"Ocorreu um erro: {e}"}


# função que filtra apenas os dados necessários
def get_weather(city_name):
    weather_data = get_weather_from_api(api_key, city_name)
    
    #CONVERSÃO DO TIMESTAMP EM DATA E HORA PADRÃO
    sunrise =  datetime.fromtimestamp(weather_data["sys"]["sunrise"])
    sunset =  datetime.fromtimestamp(weather_data["sys"]["sunset"])

    #VIEW ORGANIZADA DOS DADOS VINDOS DA API
    result = {
        "Cidade ": weather_data["name"],
        "Clima ": weather_data["weather"][0]["description"],
        "Temperatura ": f"{weather_data["main"]["temp"]} °C",
        "Umidade ": f"{weather_data["main"]["humidity"]} %",
        "Vento ": f"{weather_data["wind"]["speed"]} m/s",
        "Nascer do Sol ": sunrise,
        "Pôr do Sol ": sunset,
    }
    
    for key, value in result.items():
         print(f"{key}: {value}")
    




