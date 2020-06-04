
# coding: utf-8

# In[2]:


#Crear un histograma a partir de una lista de enteros

#[2,1,5,3]
#**
#*
#*****
#***

def crear_histograma(lista, caracter='*'):
    for e in lista:
        print(caracter * e)
        

lista = [2,1,5,3,13,7,9]
print(crear_histograma(lista))
        


