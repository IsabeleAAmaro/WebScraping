import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    ancoras = soup.find_all('a')

    print('Número de âncoras na página:', len(ancoras))
else:
    print('Falha ao obter a página:', response.status_code)
