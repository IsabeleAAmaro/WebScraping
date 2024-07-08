import re

#Questão 2

regex_unirio = r'^[a-zA-Z0-9._%+-]+@edu\.unirio\.br$'


def validar_email(email):
    if re.match(regex_unirio, email):
        return True
    else:
        return False


emails = [
    "julia@edu.unirio.br",
    "jose.ferreira@edu.unirio.br",
    "joao123@edu.unirio.br",
    "lola@unirio.br",
    "selina@edu.unirio.com",
    "mike@edu.unirio.br.other",
]

resultados = {email: validar_email(email) for email in emails}
print(resultados)
