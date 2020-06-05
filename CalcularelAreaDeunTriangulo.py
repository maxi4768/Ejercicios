
# coding: utf-8

# In[1]:


#Calcular el area de un triangulo

base = None
alture = None

while True:
    try:
        base = float(input('Escriba la base del triangulo: '))
        break
    except expression as identifier:
        print('Debe escribir un numero')
        
while True:
    try:
        altura = float(input('Escriba la altura del triangulo: '))
        break
    except expression as identifier:
        print('Debe escribir un numero')
        
area = base * altura/2

print('El area del triangulo es igual: {}'.format(area))

