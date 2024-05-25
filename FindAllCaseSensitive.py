import re

msg = ("E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você "
       "que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?")
padrao = 'e '

print("\nPadrão: " + padrao)
teste = re.search(padrao, msg)

print('\n*** search')
print(teste.group())
print('\n*** findall com case-sensitive')
teste = re.findall(padrao, msg)

print(teste)
print('\n*** findall sem case-sensitive ')

teste = re.findall(padrao, msg, re.IGNORECASE)
print(teste, "\n")
