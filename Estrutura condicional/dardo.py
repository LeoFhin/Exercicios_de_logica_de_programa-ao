#Problema "dardo" 

#No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir. 
#Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual 
#foi a maior. 

#Exemplo 1: 

#Digite as tres distancias: 
#83.21 
#79.53 
#89.15 
#MAIOR DISTANCIA = 89.15 

#Exemplo 2: 

#Digite as tres distancias: 
#83.21 
#87.20 
#83.21 
#MAIOR DISTANCIA = 87.20 

dardo1 = float(input('digite o distacia percorrida do dardo: '))
dardo2 = float(input('digite o distacia percorrida do dardo: '))
dardo3 = float(input('digite o distacia percorrida do dardo: '))

if dardo1 >= dardo2 and dardo1 >= dardo3:
    maior_distancia = dardo1
elif dardo2 >= dardo3:
    maior_distancia = dardo2
else:
    maior_distancia = dardo3

print(f'MAIOR DISTANCIA: {maior_distancia}')