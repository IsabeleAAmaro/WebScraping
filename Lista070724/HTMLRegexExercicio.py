import requests
from bs4 import BeautifulSoup
import re

# Questão 5

url = "https://bsi.uniriotec.br/institucional/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    paragrafos = soup.find_all('p')
    count_graduacao = sum(1 for p in paragrafos if p.text.lower().count('graduação') > 1)

    tags = [tag.name for tag in soup.find_all()]
    tags_unicas = set(tags)

    div_classes = set()
    for div in soup.find_all('div'):
        if 'class' in div.attrs:
            div_classes.update(div['class'])

    styles = soup.find_all(style=re.compile("color"))
    cores = set()
    for tag in styles:
        style = tag['style']
        match = re.search(r'color:\s*([^;]+)', style)
        if match:
            cores.add(match.group(1).strip())

    imagens = soup.find_all('img')
    tipos_imagem = set()
    for img in imagens:
        if 'src' in img.attrs:
            tipo = img['src'].split('.')[-1]
            tipos_imagem.add(tipo)

    print(f"a) Número de parágrafos com 'graduação' mais de uma vez: {count_graduacao}")
    print(f"b) Tags usadas na página: {tags_unicas}")
    print(f"c) Classes existentes na tag div: {div_classes}")
    print(f"d) Cores usadas na página: {cores}")
    print(f"e) Tipos de imagem na página: {tipos_imagem}")
else:
    print("Erro ao acessar a página")
