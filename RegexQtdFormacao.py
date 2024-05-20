import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')
paragrafos = soup.find_all('p')
padrao = 'formação'
cont = 0

for paragrafo in paragrafos:
    teste = re.findall(padrao, paragrafo.text)
    if len(teste) > 0:
        cont += 1

print("Quantidade 'formação': ", cont)
padrao = r'\bformação\b'
cont = 0

for paragrafo in paragrafos:
    teste = re.findall(padrao, paragrafo.text)
    if len(teste) > 0:
        cont += 1

print("Quantidade '\\bformação\\b': ", cont)