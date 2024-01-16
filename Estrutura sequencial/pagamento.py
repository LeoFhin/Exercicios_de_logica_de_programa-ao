#Problema "pagamento" 

#Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a 
#quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com 
#uma mensagem explicativa, conforme exemplo. 

#Exemplo 1: 

#Nome: Joao Silva
#Valor por hora: 50.00
#Horas trabalhadas: 60
#O pagamento para Joao Silva deve ser 3000.00 

#Exemplo 2: 

#Nome: Maria Dias
#Valor por hora: 60.00
#Horas trabalhadas: 100
#O pagamento para Maria Dias deve ser 6000.00 

nome = str(input('Digite o nome do funcionario: '))
valor_da_hora = int(input('Digite o valor por hora do funcionario: '))
horas_trabalhadas = int(input('Digite as horas trabalhas do funcionario: '))
pagamento = valor_da_hora * horas_trabalhadas

print(f'Nome: {(nome)} \n Valor da hora: {(valor_da_hora)} \n Horas Trabalhadas: {(horas_trabalhadas)} \n O Pagamento para {(nome)} deve ser de {(pagamento)}. ')