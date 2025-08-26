# CONSUMINDO API DE METEREOLOGIA
from functions import get_weather

if __name__ == "__main__":
    
    city_name = input("Qual o nome da cidade ?\n")
    get_weather(city_name)
    