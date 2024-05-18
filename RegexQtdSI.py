import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://bsi.uniriotec.br/institucional/')
soup = BeautifulSoup(res.content, 'html.parser')

find_info = re.compile(r'informação', re.IGNORECASE)
info_count = len(find_info.findall(soup.text))
find_sys = re.compile(r'sistemas', re.IGNORECASE)
sys_count = len(find_sys.findall(soup.text))

print(f'Informações: {info_count}')
print(f'Sistemas: {sys_count}')
