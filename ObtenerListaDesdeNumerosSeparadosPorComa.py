#Obtener un conjunto de numeros Separados por coma y obtener una lista

#2,8,9,0,1,2

entrada = input('Escriba varios numeros separados por coma: ')

print(entrada)
print(type(entrada))

numeros = entrada.split(',')

print(type(numeros))
print(numeros)