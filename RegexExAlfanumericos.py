import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')
texto = soup.get_text()
padrao = r'[^A-ZÀ-Üa-zà-ü0-9\s]'
caracteres = re.findall(padrao, texto)

print(set(caracteres))
print("Quantidade = ", len(caracteres))
