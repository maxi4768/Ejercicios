
# coding: utf-8

# In[4]:


# Crear una subcadena de n caracteres replicada n cantidad de veces

#'Python', n = 2 => 'PY'; 'PyPy'

def replicar_subcadena(cadena,n):
    n_caracteres = n
    
    if n_caracteres > len(cadena):
        n_caracteres = len(cadena)
        
    subcadena = cadena[0:n_caracteres]
    
    resultado = ''
    
    for i in range(n):
        resultado += subcadena
    
    return resultado

print(replicar_subcadena('Python', 2))
print(replicar_subcadena('Python', 10))

