import re

#Questão 1

string = "1227 122228 104 1222222226 1232323 1523 121212512 250"

num_com_7 = re.findall(r'\b\d*7\d*\b', string)
num_com_2_5 = re.findall(r'\b(?=\d*2)(?=\d*5)\d+\b', string)

print("Itens com dígito 7:", num_com_7)
print("Itens com dígitos 2 e 5:", num_com_2_5)
