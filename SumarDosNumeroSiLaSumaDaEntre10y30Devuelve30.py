
# coding: utf-8

# In[2]:


#Sumar 2 numeros, si la suma esta entre 10 y 30, retornar 30

def sumar(x,y):
    """
    Suma 2 numeros, si la suma esta entre 10 y 30, se retorna 30
    """
    suma = x +y
    if suma in range (10,30 +1):
        return 30
    else:
        return suma
    
print(sumar(7,3))
print(sumar(7,23))
print(sumar(12,17))
print(sumar(21,17))
    

