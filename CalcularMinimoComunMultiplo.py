
# coding: utf-8

# In[3]:


#Calcular el minimo comun multiplo

#MCM: Es el numeros positivo mas pequeño que es multiplo de dos numeros

def mcm(x,y):
    z = max(x,y)
    
    while True:
        if(z % x == 0) and (z % y == 0):
            return z
        
        z += 1
        
print(mcm(2,4))
print(mcm(2,13))
print(mcm(2,32))
print(mcm(15,17))
        
            
        
        

