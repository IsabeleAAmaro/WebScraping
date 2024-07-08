import re

# Questão 3

regex_cpf_cnpj = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'


def validar_cpf_cnpj(id):
    if re.match(regex_cpf_cnpj, id):
        return True
    else:
        return False


id = [
    "123.456.789-09",
    "12.345.678/0001-95",
    "123.456.789-0a",
    "12.345.678/0001-9",
    "12345678909",
    "123456789000195",
]

resultados = {id: validar_cpf_cnpj(id) for id in id}
print(resultados)
