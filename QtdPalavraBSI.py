import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')
soup = BeautifulSoup(response.text, 'html.parser')
texto_pagina = soup.get_text()

ocorrencias_bsi = texto_pagina.lower().count('bsi')
print('Número de vezes que a palavra "BSI" aparece na página:', ocorrencias_bsi)
