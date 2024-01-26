#Problema "aumento" (adaptado de URI 1048) 

#Uma empresa vai conceder um aumento percentual de 
#salário aos seus funcionários dependendo de quanto 
#cada pessoa ganha, conforme tabela ao lado. Fazer um 
#programa para ler o salário de uma pessoa, daí mostrar 
#qual o novo salário desta pessoa depois do aumento, 
#quanto foi o aumento e qual foi a porcentagem de 
#aumento. 

# Salário atual Aumento 

#Até R$ 1000.00 20% 

#Acima de R$ 1000.00   
#até R$ 3000.00 
#15% 

#Acima de R$ 3000.00 
#até R$ 8000.00 
#10% 

#Acima de R$ 8000.00 5% 

#Exemplo 1: 

#Digite o salario da pessoa: 2500.00 
#Novo salario = R$ 2875.00 
#Aumento = R$ 375.00 
#Porcentagem = 15 % 

#Exemplo 2: 

#Digite o salario da pessoa: 8000.00 
#Novo salario = R$ 8800.00 
#Aumento = R$ 800.00 
#Porcentagem = 10 % 

salario = float(input('Digite o seu salario: '))

if salario <= 1000:
    porcentagem = 20
    reajuste = salario * porcentagem / 100
    novo_salario = salario + reajuste

elif salario <= 3000:
    porcentagem = 15
    reajuste = salario * porcentagem / 100
    novo_salario = salario + reajuste

elif salario <= 8000:
    porcentagem = 10
    reajuste = salario * porcentagem / 100
    novo_salario = salario + reajuste

else:
    porcentagem = 5
    reajuste = salario * porcentagem / 100
    novo_salario = salario + reajuste 

print(f'Novo salario = R${novo_salario:.2f} \n Aumento = R${reajuste:.2f} \n Porcentagem = {porcentagem}%')

