import requests
from bs4 import BeautifulSoup

# Faz a requisição GET
response = requests.get('https://bsi.uniriotec.br')

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisa o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todos os parágrafos que contêm a palavra "BSI"
    paragrafos_com_bsi = soup.find_all('p', string=lambda text: 'BSI' in (text or ''))
    
    # Imprime o número de parágrafos com a palavra "BSI"
    print('Número de parágrafos com a palavra "BSI":', len(paragrafos_com_bsi))
else:
    print('Falha ao obter a página:', response.status_code)
