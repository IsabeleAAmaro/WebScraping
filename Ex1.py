import requests, bs4
r = requests.get('https://bsi.uniriotec.br')
pagina = bs4.BeautifulSoup(r.text, "html.parser")
links = pagina.find_all('a')
print('Quantidade de links =', len(links))
for link in links:
    print(link.get('href'))