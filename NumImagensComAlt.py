import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    imagens_com_alt = soup.find_all('img', alt=True)

    print('Número de imagens com o atributo alt:', len(imagens_com_alt))
else:
    print('Falha ao obter a página:', response.status_code)
