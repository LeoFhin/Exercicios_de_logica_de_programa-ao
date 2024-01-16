#Problema "troco" 

#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, 
#e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve 
#mostrar o valor do troco a ser devolvido ao cliente. 

#Exemplo 1: 

#Preço unitário do produto: 8.00
#Quantidade comprada: 2
#Dinheiro recebido: 20.00
#TROCO = 4.00 

#Exemplo 2: 

#Preço unitário do produto: 30.00
#Quantidade comprada: 3
#Dinheiro recebido: 100.00
#TROCO = 10.00 


#ex1

valorproduto1 = 8.00

compras = float(input('digite aqui a quantidade de itens que voce gostaria de comprar: '))

quantidade1 = valorproduto1 * compras


dinheiro_recebido = float(input('digite aqui o valor pago: '))

troco1 = dinheiro_recebido - quantidade1

print(f'O seu troco é de: {(troco1)}')




