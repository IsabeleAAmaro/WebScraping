import requests
from bs4 import BeautifulSoup
import re

url = 'https://bsi.uniriotec.br/institucional/'
response = requests.get(url)
pagina = BeautifulSoup(response.text, 'html.parser')
texto = pagina.body.text

numeros = re.findall(r'\d{1,}', texto)
print(numeros)
# Conta o número de números encontrados
total_numeros = len(numeros)
print(f"Total de números com mais de um dígito: {total_numeros}")
