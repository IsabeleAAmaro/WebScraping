import requests
from bs4 import BeautifulSoup

response = requests.get('https://bsi.uniriotec.br')
soup = BeautifulSoup(response.text, 'html.parser')
texto_pagina = soup.get_text()

ocorrencias_bsi = texto_pagina.lower().count('bsi')
print('Número de vezes que a palavra "BSI" aparece na página:', ocorrencias_bsi)

""" 17. name: Retorna o nome da tag.
attrs: Retorna um dicionário contendo todos os atributos da tag e seus valores
get_text(): Retorna o texto contido dentro da tag e de todas as suas tags filhas, de forma concatenada.

18. NavigableString é uma classe que representa uma string ou texto encontrado dentro de uma tag, 
ela pode ser usada para manipular o conteúdo textual de uma tag específica. A NavigableString possui métodos como strip() 
para remover espaços em branco ao redor do texto, replace_with() para substituir o texto por outro e find() para buscar substrings dentro do texto.

19) find_all() é um método do BeautifulSoup que busca por todas as ocorrências de uma determinada tag e 
retorna uma lista com os resultados. select() é um método que permite buscar elementos usando seletores CSS. 
Ele retorna uma lista de todos os elementos que correspondem ao seletor especificado.

20) O atributo .string é usado para acessar o conteúdo textual de uma tag, caso haja apenas texto direto dentro dela. 
Ele retorna o conteúdo textual como uma string ou None se a tag não contiver texto direto.

21) O atributo .text é usado para acessar todo o conteúdo textual de uma tag, incluindo o texto de suas tags filhas. 
Ele retorna o conteúdo textual concatenado como uma string.

22. O atributo .string retorna apenas o texto direto dentro de uma tag, enquanto o atributo .text retorna todo o conteúdo textual da tag, 
incluindo o texto de suas tags filhas.

23) Na prática, não há diferença entre .string e .text quando se trata de tags que contêm apenas texto direto, 
ois ambos retornarão o mesmo resultado. No entanto, quando a tag contém mais de um nível de texto aninhado, o .string retornará None,
 enquanto o .text retornará o conteúdo textual completo.

24) O atributo .contents é usado para acessar a lista de todos os elementos filhos diretos de uma tag. 
Ele retorna uma lista com os elementos filhos diretos da tag.

25) O atributo .parent é usado para acessar o elemento pai de uma tag. Ele retorna o elemento pai da tag.

26) .next_sibling é usado para acessar o próximo irmão da tag (ou seja, o elemento imediatamente após a tag no mesmo nível de hierarquia) e 
next_element é usado para acessar o próximo elemento (tag ou string) na árvore de análise, independentemente de ser irmão ou não.

27) O método find_next_siblings() é usado para encontrar todos os irmãos seguintes de uma tag 
que correspondem aos critérios de busca especificados.

28)O html.parser é um analisador HTML incorporado do Python que faz parte da biblioteca padrão. 
Ele é usado pelo BeautifulSoup para analisar o código HTML e construir a árvore de análise que representa a estrutura do HTML.

29) Sim, existem outras alternativas para o html.parser do BeautifulSoup, como lxml

31. Regex são sequências de caracteres que definem um padrão de busca em textos. 

33. é uma linguagem de consulta usada para navegar e selecionar elementos em documentos XML ou HTML. 

30) O parâmetro recursive=True indica ao método find() que ele deve procurar recursivamente por elementos dentro de elementos, ou seja, 
ele deve procurar não apenas nos filhos diretos, mas também em todos os descendentes da tag especificada. S
e recursive=False, o método find() só procurará pelos filhos diretos da tag especificada."""
