# Solicitar al usuario un numero y calculadar sumatorio

# 3 = 3 = 3 + 33 + 333 = 369

n = input('Escriba el valor de n: ')

nn = int('{}{}'.format(n,n))
nnn = int('%s%s%s' % (n,n,n))
n = int(n)

suma = n + nn + nnn

print(suma)