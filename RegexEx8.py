import re

msg = ('E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você '
       'que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?')

padrao = r'a'
print("Padrão: r'a' - quantidade de letras 'a'")
teste = re.findall(padrao, msg)
print(teste)
print('\n')

padrao = r'[^a]'
print("Padrão: r'[^a]' - letras que não são 'a'")
teste = sorted(set(re.findall(padrao, msg)))
print(teste)
print('\n')

padrao = r'^a'
print("Padrão: r'^a' - a string começa com 'a'?")
teste = re.findall(padrao, msg)
print(teste)
print('\n')