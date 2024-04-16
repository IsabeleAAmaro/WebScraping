import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    todos_paragrafos = soup.find_all('p')

    menor_paragrafo = None
    tamanho_menor_paragrafo = float('inf')

    for paragrafo in todos_paragrafos:
        texto_paragrafo = paragrafo.get_text().strip()

        if texto_paragrafo:
            tamanho_paragrafo = len(texto_paragrafo)

            if tamanho_paragrafo < tamanho_menor_paragrafo:
                tamanho_menor_paragrafo = tamanho_paragrafo
                menor_paragrafo = texto_paragrafo

    if menor_paragrafo:
        print('O menor parágrafo não vazio da página é:')
        print(menor_paragrafo)
    else:
        print('Não foi encontrado nenhum parágrafo não vazio na página.')
else:
    print('Falha ao obter a página:', response.status_code)

