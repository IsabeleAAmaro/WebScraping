import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    todos_paragrafos = soup.find_all('p')

    maior_paragrafo = None
    tamanho_maior_paragrafo = 0

    for paragrafo in todos_paragrafos:
        tamanho_paragrafo = len(paragrafo.get_text())

        if tamanho_paragrafo > tamanho_maior_paragrafo:
            tamanho_maior_paragrafo = tamanho_paragrafo
            maior_paragrafo = paragrafo

    if maior_paragrafo:
        print('O maior parágrafo da página é:')
        print(maior_paragrafo.get_text())
    else:
        print('Não foi encontrado nenhum parágrafo na página.')
else:
    print('Falha ao obter a página:', response.status_code)
