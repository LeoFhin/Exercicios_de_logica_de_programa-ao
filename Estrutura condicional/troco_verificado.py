#Problema "troco_verificado" 

#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, 
#e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido 
#ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o 
#valor restante conforme exemplo. 

#Exemplo 1: 

#Preço unitário do produto: 8.00
#Quantidade comprada: 2
#Dinheiro recebido: 20.00
#TROCO = 4.00 

#Exemplo 2: 

#Preço unitário do produto: 30.00
#Quantidade comprada: 3
#Dinheiro recebido: 70.00
#DINHEIRO INSUFICIENTE. FALTAM 20.00 REAIS 

valor_do_produto = float(input('Digite o valor do produto: '))
quantidade_comprada = int(input('Digite a quantidade comprada: '))
dinheiro_recebido = float(input('Digite o dinheiro: '))

valor_a_pagar = valor_do_produto * quantidade_comprada
troco = dinheiro_recebido - valor_a_pagar
dinheiro_insuficiente = valor_a_pagar - dinheiro_recebido

if valor_a_pagar >= dinheiro_recebido:
    print(f'Dinheiro insuficiente: faltam {dinheiro_insuficiente} reais')
else:
    print(f'O seu troco é de: {troco} reais.')
