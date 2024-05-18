import requests
from bs4 import BeautifulSoup

url = "https://bsi.uniriotec.br/institucional/"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
links = soup.select("a[href]")

for link in links:
    if "unirio" in link['href']:
        print(link['href'])

print("Quantidade: ", len(links))