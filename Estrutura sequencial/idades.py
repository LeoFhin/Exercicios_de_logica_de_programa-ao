#Problema "idades" 

#Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os 
#nomes e a idade média entre essas pessoas, conforme exemplo. 

#Exemplo: 

#Dados da primeira pessoa: 
#Nome: Maria Silva
#Idade: 19

#Dados da segunda pessoa: 
#Nome: Joao Melo
#Idade 20

#A idade média de Maria Silva e Joao Melo é de 19.5 anos 

nome1 = str(input('Digite o nome da primera pessoa: '))
idade1 = int(input('digite a idade da primera pessoa: '))

nome2 = str(input('Digite o nome da segunda pessoa: '))
idade2 = int(input('digite a idade da segunda pessoa: '))

media = (idade1 + idade2) / 2

print(f'Dados da primera pessoa: \n Nome: {(nome1)} \n Idade: {(idade1)} ')
print(f'Dados da segunda pessoa: \n Nome: {(nome2)} \n Idade: {(idade2)}')
print(f'A media de {(nome1)} e {(nome2)} é de {(media)}')