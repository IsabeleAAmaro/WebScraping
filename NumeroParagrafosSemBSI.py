import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    todos_paragrafos = soup.find_all('p')

    paragrafos_sem_bsi = [p for p in todos_paragrafos if 'BSI' not in p.get_text()]

    print('Número de parágrafos sem a palavra "BSI":', len(paragrafos_sem_bsi))
else:
    print('Falha ao obter a página:', response.status_code)
