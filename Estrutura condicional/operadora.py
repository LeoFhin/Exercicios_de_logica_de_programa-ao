#Problema "operadora" 

#Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de 
#telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para 
#ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 

#Exemplo 1: 

#Digite a quantidade de minutos: 22
#Valor a pagar: R$ 50.00 

#Exemplo 2: 

#Digite a quantidade de minutos: 103
#Valor a pagar: R$ 56.00 

minutos = float(input('Digite aqui a quantidade de minutos: '))
valor_pago = 50.00

if minutos > 100:
   valor_pago = valor_pago + 2 * (minutos - 100)

print(f'Valor a pagar: {valor_pago}')