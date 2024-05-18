import requests
from bs4 import BeautifulSoup

url = "https://bsi.uniriotec.br/institucional/"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
links = soup.select("a[href='https://bsi.uniriotec.br/institucional/']")

for link in links:
    print(link['href'])

print("Número de links:", len(links))