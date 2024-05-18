import requests
from bs4 import BeautifulSoup

res = requests.get("https://bsi.uniriotec.br/institucional/")
if res.status_code == 200:
    content = res.content

soup = BeautifulSoup(content, 'html.parser')
links_externos = 0
for link in soup.find_all('a'):
    if link.get('href') and not link.get('href').startswith('#') and not link.get('href').startswith('https://bsi.uniriotec.br'):
        links_externos +=1
        print(link['href'])
        print(f"\nA página possui {links_externos} links externos.")
else:
    print("Erro ao acessar a página.")