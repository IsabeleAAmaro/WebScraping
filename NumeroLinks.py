import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)

    print('Número de links na página:', len(links))
else:
    print('Falha ao obter a página:', response.status_code)
