import bs4
import re
import requests

resp = requests.get('https://bsi.uniriotec.br/institucional')
pagina = bs4.BeautifulSoup(resp.text, "html.parser")
padrao = '\stecno\S+'
teste = re.findall(padrao, str(pagina))
print(teste)
