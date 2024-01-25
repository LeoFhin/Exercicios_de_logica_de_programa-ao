#Problema "temperatura" 

#Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para 
#isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser 
#informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com 
#duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve 
#deduzir a fórmula de Celsius para Fahrenheit): 


#Exemplo 1: 

#Voce vai digitar a temperatura em qual escala (C/F)? F
#Digite a temperatura em Fahrenheit: 75.00
#Temperatura equivalente em Celsius: 23.89 

#Exemplo 2: 

#Voce vai digitar a temperatura em qual escala (C/F)? C
#Digite a temperatura em Celsius: 28.15
#Temperatura equivalente em Fahrenheit: 82.67 

temperatura = str(input('Digite o tipo de temperatura: (C/F)?'))

if temperatura == 'F':
    fahrenheit = float(input('Digite a temperatura em fahrenheit:'))

    celsius = 5.0 / 9.0 * (fahrenheit - 32.0)
    print(f"Temperatura equivalente em celcius: {celsius:.2f} ")
else:
    celsius = float(input('Digite a temperatura em celcius: '))

    fahrenheit = celsius * 9.0 / 5.0 + 32.0;
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")
