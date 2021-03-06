
# coding: utf-8

# In[7]:


# Comprobar si un caracter dado es una vocal

# c = 'i', ['a','e','i','o','u',] )> True
# c = 'z', ['a','e','i','o','u',] )> False

def es_vocal(c):
    """
    Comprueba si un caracter es una vocal
    """
    if len(c) == 1:
        vocales = 'aeiou'
        c = c.lower()
    
        return c in vocales
    else:
        return False


print(es_vocal('i'))
print(es_vocal('z'))
print(es_vocal('b'))
print(es_vocal('A'))
print(es_vocal('ae'))
print(es_vocal('gt'))

