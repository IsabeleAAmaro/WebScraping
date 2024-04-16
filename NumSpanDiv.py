import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.find_all('div')

    spans_filhos_de_div = 0

    for div in divs:
        spans_filhos = div.find_all('span')

        if spans_filhos:
            spans_filhos_de_div += len(spans_filhos)

    print('Número de spans filhos de divs:', spans_filhos_de_div)
else:
    print('Falha ao obter a página:', response.status_code)
