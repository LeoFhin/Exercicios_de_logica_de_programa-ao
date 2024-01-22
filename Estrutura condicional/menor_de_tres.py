#Problema "menor_de_tres" 

#Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três 
#números lidos. Em caso de empate, mostrar apenas uma vez. 

#Exemplo 1: 

#Primeiro valor: 7
#Segundo valor: 3
#Terceiro valor: 8
#MENOR = 3 

#Exemplo 2: 

#Primeiro valor: 5
#Segundo valor: 12
#Terceiro valor: 5
#MENOR = 5 

#Exemplo 3: 

#Primeiro valor: 9
#Segundo valor: 9
#Terceiro valor: 9
#MENOR = 9 

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

if valor1 <= valor2 and valor1 <= valor3:
    print(f'Menor número: {valor1}')
elif valor2 <= valor3:
        print(f'menor número: {valor2}')
else: 
        print(f'menor número: {valor3}')