import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

response = requests.get('https://bsi.uniriotec.br')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    links_internos = 0
    url_base = urlparse(response.url).scheme + '://' + urlparse(response.url).netloc

    for link in links:
        if link['href'].startswith('/'):
            links_internos += 1
    print('Número de links internos na página:', links_internos)
else:
    print('Falha ao obter a página:', response.status_code)
