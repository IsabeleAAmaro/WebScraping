import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')
texto = soup.get_text()
padrao = r'\b\w+ver\w+\b'
palavras = re.findall(padrao, texto)

for palavra in palavras:
    print(palavra)

print("Quantidade = ", len(palavras))
