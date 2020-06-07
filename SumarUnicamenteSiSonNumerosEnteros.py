
# coding: utf-8

# In[6]:


#Crear una funcion unicamente para sumar numeros enteros

def sumar(x,y):
    if isinstance(x, int) and isinstance(y,int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros')

try:
    print(sumar(2,3))
     print(sumar(2,a))
except TypeError as e:
    print(e)


    

