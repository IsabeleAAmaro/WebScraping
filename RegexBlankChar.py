import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')
texto = soup.get_text()
padrao = r'\s'
brancos = re.findall(padrao, texto)
print("Quantidade = ", len(brancos))