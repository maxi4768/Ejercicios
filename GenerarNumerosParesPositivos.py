
# coding: utf-8

# In[1]:


#Generar los n primeros numeros pares positivos.

def generar_numeros_pares(n = 100):
    """
    Genera los n primero numeros pares positivos
    """
    pares = []
    
    contador = 0
    numero = 0
    
    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        
        numero += 1
    
    return pares

n = int(input('Escriba la cantidad de numeros pares positivos a generar: '))

if n > 0:
        pares = generar_numeros_pares(n)
        
        print(pares)
        print('Cantidad de pares:',len(pares))
else:
        print('El numero debe ser positivo')



