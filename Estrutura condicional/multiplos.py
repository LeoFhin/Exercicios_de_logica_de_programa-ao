#Problema "multiplos" (adaptado de URI 1044)

#Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os 
#números podem ser digitados em qualquer ordem. 

#Exemplo 1: 

#Digite dois numeros inteiros: 
#6
#24
#Sao multiplos 

#Exemplo 2: 

#Digite dois numeros inteiros: 
#24
#6
#Sao multiplos

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um outro numero inteiro: '))

if num1 % num2 == 0 or num2 % num1 == 0:
    print('São multiplos')
else:
    print('Não sao multiplos')