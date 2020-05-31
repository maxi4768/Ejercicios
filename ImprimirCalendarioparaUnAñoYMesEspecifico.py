#Imprimir el calendario para un año y mes especifico
import calendar 

agnio =int(input("Escriba el año: "))
mes = int(input("Escriba el mes: "))

print(calendar.month(agnio, mes))

