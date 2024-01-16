#Problema "terreno"
#Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular, 
#bem como o valor do metro quadrado do terreno. Em seguida, o programa deve mostrar
#o valor da área do terreno, bem como o valor do preço do terreno,
#conforme exemplo.

#Exemplo 1:
#Digite a largura do terreno: 10.0
#Digite o comprimento do terreno: 30.0
#Digite o valor do metro quadrado: 200.00
#Area do terreno = 300.00
#Preco do terreno = 60000.00

#Exemplo 2:
#Digite a largura do terreno: 12.0
#Digite o comprimento do terrano: 20.0
#Digite o valor do metro quadrado: 150.00
#Area do terreno = 240.00
#Preco do terreno = 36000.00 #

largura = float(input('digite a largura do terreno: '))
comprimento = float(input('digite o comprimento do terreno: '))
preco_do_metro_quadrado = float(input('digite o preço do metro quadrado: '))

area = largura * comprimento
preco = area * preco_do_metro_quadrado

print(f'o valor da area é {(area)}')
print(f'o preço do terreno é {(preco)}')