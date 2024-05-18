msg = 'O Bacharelado ....'

tam_msg = len(msg)
palavra = input("\nDigite texto a ser pesquisado: ")
tam_palavra=len(palavra)
num = 0

for i in range(tam_msg):
    texto = msg[i:i+tam_palavra]
if texto.lower() == palavra.lower():
    num += 1
    print(str(num) + " - palavra: " + texto + ", posição inicial: " + str(i))
if num == 0:
    print("Texto não encontrado")
    print('\n*** Fim da pesquisa\n')