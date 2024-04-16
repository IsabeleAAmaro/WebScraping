import requests
from bs4 import BeautifulSoup

r = requests.get('https://bsi.uniriotec.br')
pagina = BeautifulSoup(r.text, "html.parser")

paragrafos_com_classe = pagina.select('p[class]')
print("Número de parágrafos com classe CSS:", len(paragrafos_com_classe))
