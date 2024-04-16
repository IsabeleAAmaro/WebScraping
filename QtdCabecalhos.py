import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    cabecalhos = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print('Número de cabeçalhos na página:', len(cabecalhos))
else:
    print('Falha ao obter a página:', response.status_code)
