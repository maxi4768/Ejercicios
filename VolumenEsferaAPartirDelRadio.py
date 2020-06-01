#Calcular el volumen de una esfera a partir del radio dado.
#WolframAlpha pagina interesante
from math import pi

r = float(input('Debe ingresar el radio de la esfera: '))

volumen = 4/3 * pi * r ** 3

print("El volumen de la esfera es {} unidades cubicas".format(volumen))




