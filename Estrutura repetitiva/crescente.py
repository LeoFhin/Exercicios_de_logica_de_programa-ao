#Problema "crescente" (adaptado de URI 1113) 

#Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma 
#mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O 
#programa deve finalizar quando forem digitados dois valores iguais. 

#Exemplo: 

#Digite dois numeros: 
#5 
#4 

#DECRESCENTE! 

#Digite outros dois numeros: 
#3 
#8 

#CRESCENTE! 

#Digite outros dois numeros: 
#2 
#2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while num1 != num2:
    if num1 > num2:
        print('DESCRESCENTE!')
    
    else:
        print('CRESCENTE')

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: ')) 