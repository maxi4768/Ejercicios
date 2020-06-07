
# coding: utf-8

# In[3]:


#Clase Persona

class Persona:
    def __init__(self,nombre,edad,correo):  #constructor clase Persona
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre,self.edad,self.correo)
    
edward = Persona('Edward','33','edward@mail.co')

print(edward)

