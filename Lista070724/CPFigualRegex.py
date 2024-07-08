import re

# Questão 4

regex_cpf = (r'^(\d{3})\.\d{3}\.\1-\d{2}$|^(\d{3})\.\2\.\d{3}-\d{2}$|^(\d{3})\.\d{3}\.\d{3}-\d{2}$|^(\d{3})\.\d{'
             r'3}\.\2-\d{2}$|^(\d{3})\.\d{3}\.\3-\d{2}$|^(\d{3})\.\3\.\d{3}-\d{2}$')

cpfs = [
    "123.456.123-78",
    "435.981.981-78",
    "123.123.123-78",
    "111.222.333-44",
    "123.456.789-01",
]


def selecionar_cpfs_iguais(lista_cpfs):
    return [cpf for cpf in lista_cpfs if re.match(regex_cpf, cpf)]


cpfs_selecionados = selecionar_cpfs_iguais(cpfs)
print(cpfs_selecionados)
