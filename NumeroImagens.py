import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    imagens = soup.find_all('img')

    print('Número de imagens na página:', len(imagens))
else:
    print('Falha ao obter a página:', response.status_code)
