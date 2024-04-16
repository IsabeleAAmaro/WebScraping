import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elementos_menu_item = soup.find_all(class_='menu-item')

    print('Número de elementos com a classe "menu-item":', len(elementos_menu_item))
else:
    print('Falha ao obter a página:', response.status_code)
