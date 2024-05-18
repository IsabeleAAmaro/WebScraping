import re

msg = ('E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você '
       'que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?')
print('\n')

padrao = 'Jos[é]'
print('Padrão: "Jos[é]"')
teste = re.findall(padrao, msg)
print(teste, "\n")

print('Padrão: "Jos[a-zá-ü]"')
padrao = "Jos[a-zá-ü]"
teste = re.findall(padrao, msg)
print(teste, "\n")

print('Padrão: "Jos[\w]"')
padrao = "Jos[\w]"
teste = re.findall(padrao, msg)
print(teste, "\n")