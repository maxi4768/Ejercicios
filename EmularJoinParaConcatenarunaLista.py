
# coding: utf-8

# In[3]:


#Emular el funcionamiento de la funcion join para concatenar lista

#numeros = [2,3,5,7,11]

#print(''.join([str(n) for n in numeros]))

def concatenar_lista(lista):
    resultado = ''
    
    for n in lista:
        resultado += str(n)
        
    return resultado

numeros = [2,3,4,7,8,11]

print(concatenar_lista(numeros))

