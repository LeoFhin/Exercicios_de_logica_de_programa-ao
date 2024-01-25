#Problema "lanchonete" (adaptado de URI 1038)

#Uma lanchonete possui vários produtos. Cada produto possui um código 
#e um preço. Você deve fazer um programa para ler o código e a 
#quantidade comprada de um produto (suponha um código válido), e daí 
#informar qual o valor a ser pago, com duas casas decimais, conforme 
#tabela de produtos ao lado. 

#Código do 
#produto 
#Preço do 
#produto 

#1 R$ 5.00 
#2 R$ 3.50 
#3 R$ 4.80 
#4 R$ 8.90 
#5 R$ 7.32 

#Exemplo 1: 

#Codigo do produto comprado: 1
#Quantidade comprada: 3
#Valor a pagar: R$ 15.00 

#Exemplo 2: 

#Codigo do produto comprado: 4
#Quantidade comprada: 2
#Valor a pagar: R$ 17.80 

codigo = int(input('Digite o codigo do produto (de 1 a 5): '))
quantidade = int(input('Digite a quantidade de produtos: '))

p1 = 5.00
p2 = 3.50
p3 = 4.80
p4 = 8.90
p5 = 7.32

if codigo == 1:
    valor_a_pagar = p1 * quantidade
elif codigo == 2:
    valor_a_pagar = p2 * quantidade
elif codigo == 3:
    valor_a_pagar = p3 * quantidade
elif codigo == 4:
    valor_a_pagar = p4 * quantidade
elif codigo == 5:
    valor_a_pagar = p5 * quantidade

print(f'Valor a pagar: {valor_a_pagar:.2f}')


