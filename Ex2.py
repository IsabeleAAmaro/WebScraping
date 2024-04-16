import requests, bs4
r = requests.get('https://bsi.uniriotec.br')
pagina = bs4.BeautifulSoup(r.text, "html.parser")
links = pagina.select('a[href]')
print("\nNúmero de links: " + str(len(links)))
for link in links:
    print(link)