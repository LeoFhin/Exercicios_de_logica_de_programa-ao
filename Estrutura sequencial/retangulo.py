import math

#Problema "retangulo" 

#Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor 
#da área, perímetro e diagonal deste retângulo, conforme exemplos. 

#Exemplo 1: 
#Base do retangulo: 4.0
#Altura do retangulo: 5.0
#AREA = 20.0000 
#PERIMETRO = 18.0000 
#DIAGONAL = 6.4031 

#Exemplo 2: 
#Base do retangulo: 10.3
#Altura do retangulo: 13.1
#AREA = 134.9300 
#PERIMETRO = 46.8000 
#DIAGONAL = 16.6643

base = float(input('digite a área do rentagulo: '))
altura = float(input('digite a altura do retangulo: '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = ((base * base) + (altura * altura)) * 0.5

print(f'o valor da area é: {(area)} ')
print(f'o valor do perimetro é: {(perimetro)}') 
print(f'o valor da diagonal é: {(diagonal)}')