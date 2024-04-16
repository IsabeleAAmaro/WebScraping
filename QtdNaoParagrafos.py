import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')
soup = BeautifulSoup(response.text, 'html.parser')
tags = soup.find_all(True)

total_tags_nao_paragrafos = sum(1 for tag in tags if tag.name != 'p')

print('Número de tags que não são parágrafos:', total_tags_nao_paragrafos)
