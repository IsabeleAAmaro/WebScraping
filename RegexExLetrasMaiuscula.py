import requests
import re
from bs4 import BeautifulSoup

url = "https://bsi.uniriotec.br/institucional/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
texto = soup.get_text()

padrao = r'\b[A-ZÀ-Ü][a-zà-ü]*\b'
palavras = re.findall(padrao, texto)
print(palavras)
print("Quantidade = ", len(palavras))
