# Obtener la fecha y hora actuales en el sistema
import datetime  #modulo que viene por defectgo con la instalacion

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))