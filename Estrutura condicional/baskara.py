#Problema "baskara" 
#Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula 
#de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais, 
#conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. 

#Exemplo 1: 

#Coeficiente a: 1
#Coeficiente b: 0
#Coeficiente c: -9
#X1 = 3.0000 
#X2 = -3.0000 

#Exemplo 2: 
#Coeficiente a: 2
#Coeficiente b: -4.5
#Coeficiente c: 1.7
#X1 = 1.7697 
#X2 = 0.4803 

#Exemplo 3: 
#Coeficiente a: 1
#Coeficiente b: 3
#Coeficiente c: 4
#Esta equacao nao possui raizes reais

import math

a = float(input('DIGITE O VALOR DE A:'))
b = float(input('DIGITE O VALOR DE B: '))
c = float(input('DIGITE O VALOR DE C: '))

delta = (b * b) -(4 * a * c)

if delta < 0: 
    print('esssa equaçao nao possui raizes reais')
else:
    baskara1 = ((-b) + math.sqrt(delta)) / (2 * a)
    baskara2 = ((-b) - math.sqrt(delta)) / (2 * a)

    print(f'X1 = {baskara1:.4f}')
    print(f'X2 = {baskara2:.4f}')


