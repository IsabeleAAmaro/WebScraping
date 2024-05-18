import re

msg = ('E agora, José? A festa acabou, a luz apagou, o povo sumiu, a noite esfriou, e agora, José? e agora, você? você '
       'que é sem nome, que zomba dos outros, você que faz versos, que ama, protesta? e agora, José?')

print('\n')
padrao = 'a[abc]a[abc]ou'
print('Padrão: "a[abc]a[abc]ou"')
teste = re.findall(padrao, msg)
print(teste)

print('\n')
padrao = 'a[a-z]a[bg]ou'
print('Padrão: "a[a-z]a[bg]ou"')
teste = re.findall(padrao, msg)
print(teste)
print('\n')
