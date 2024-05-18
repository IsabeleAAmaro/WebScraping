import requests
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')

paragrafos = soup.find_all('p')
cont = 0
for paragrafo in paragrafos:
    if "sistemas" in paragrafo.text.lower() and "curso" in paragrafo.text.lower():
        print("\n", paragrafo.text)
        cont += 1

print("Quantidade =", cont)
