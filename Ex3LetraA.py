import requests
from bs4 import BeautifulSoup
resposta = requests.get('https://bsi.uniriotec.br')

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    primeiro_paragrafo = soup.find('p')

    if primeiro_paragrafo:
        print('Tag completa do primeiro parágrafo:')
        print(primeiro_paragrafo)
    else:
        print('Nenhum parágrafo encontrado na página.')
else:
    print('Falha ao obter a página:', resposta.status_code)
