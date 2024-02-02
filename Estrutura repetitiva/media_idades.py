#Problema "media_idades" 

#Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um 
#indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular 
#e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, 
#mostrar a mensagem "IMPOSSIVEL CALCULAR". 

#Exemplo 1: 

#Digite as idades: 

#31 
#27 
#46 
#-5 

#MEDIA = 34.67 

#Exemplo 2: 

#Digite as idades: 
#-10 

#IMPOSSIVEL CALCULAR

print('Dígite as idades: ')
idade = int(input())

if idade < 0:
    print(f'IMPOSSIVEL CALCULAR')
else:
    soma = 0
    cont = 0

    while idade >= 0:
        soma = soma + idade
        cont = cont + 1
        idade = int(input())

    media = soma / cont

    print(f'MEDIA = {media:.2f}')