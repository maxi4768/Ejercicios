
# coding: utf-8

# In[7]:


# Simular el funcionamiento del operador in

#print(5 in [2,3,4,5,7,11])
#print('k' in 'Fork')
#print('i' in 'Fork')
"""
Comprueba si un elemento esta disponible en una lista
"""

def pertenece_a(lista, elemento):

    for e in lista:
        if elemento == e:
            return True
        
    return False

print(pertenece_a([2,3,4,5,7,11],5))
print(pertenece_a([2,3,4,5,7,11],19))
print(pertenece_a('fork','k'))
print(pertenece_a('fork','i'))

print()

print(pertenece_a(['F','o','r','k'],'k'))
print(pertenece_a(['F','o','r','k'],'i'))

