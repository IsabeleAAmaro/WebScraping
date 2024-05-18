import re

msg = ('E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você '
       'que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?')
print('\n')

padrao = 'a.a.ou'
print('Padrão: "a.a.ou" onde 1 ponto = 1 caractere')
teste = re.findall(padrao, msg)

print(teste)
print('\n')

padrao = '....ou'
print('Padrão: "....ou" com 4 caracteres antes de "ou"')

teste = re.findall(padrao, msg)
print(teste)
print('\n')
