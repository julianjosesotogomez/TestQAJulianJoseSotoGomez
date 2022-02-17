# coding: utf-8
# Your code here!
from datetime import date #Esta libreria me permite identificar y validar la fecha que estoy ingresamdo
date_one = date(2022,10,20) #Ingreso la fecha a la cual la voy a comparar con la fecha actual
date_today = date.today() # Fecha actuaql de la comparativa 
operation_date = (date_one - date_today).days #Comparativa de la fecha ingresada en la variable data_one con date_today
print(f"Diferencia de días --> {operation_date} días de diferencia") #Salida por consola "245" días de diferencia
#-----------------------------------------------------------------------------