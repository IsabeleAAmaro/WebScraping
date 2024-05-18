msg = ("O Bacharelado em Sistemas de Informação da UNIRIO é um urso vespertino/noturno de graduação com duração "
       "prevista de 4 anos, com carga horária total de 3.240 horas-aula em regime de crédito semestral. Atualmente o "
       "curso BSI-UNIRIO oferece 72 vagas anuais, com duas entradas semestrais de 36 alunos através do Sistema de "
       "Seleção Unificado (SiSU), que é o processo seletivo baseado no resultado do Exame Nacional do Ensino Médio ("
       "ENEM).")

palavra = input("\nDigite texto a ser pesquisado: ")
if palavra.lower() in msg.lower():
    print("Existe a palavra '" + palavra + "' na mensagem", )
else:
    print("A palavra '" + palavra + "' não existe na mensagem")