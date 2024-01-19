#Problema "notas" 

#Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestree s d
#uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal)no 
#ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a 
#mensagem "REPROVADO", conforme exemplos. 

#Exemplo 1: 

#Digite a primeira nota: 45.5
#Digite a segunda nota: 31.3
#NOTA FINAL = 76.8 

#Exemplo 2: 

#Digite a primeira nota: 34.0
#Digite a segunda nota: 23.5
#NOTA FINAL = 57.5 
#REPROVADO

semestre1 = float(input('Digite a nota do primeiro semestre: '))
semestre2 = float(input('digite a nota do segundo semestre: '))

media = semestre1 + semestre2

if media >= 60.00:
    print(f'Voce foi aprovado!!! \n Nota final: {(media)}')
else:
    print(f'voce foi reprovado :( \n Nota final: {(media)} ')