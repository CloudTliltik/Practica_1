#Algoritmo para calcular el numero de dias que has vivido hasta el 23 de marzo.
#Los ejecicios asignados son los (2)
import datetime

#Se nececesita el día, mes y año

dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))

# Se crea un bojeto datetime
fecha_nacimiento = datetime.datetime(anio, mes, dia)
#Se ocupa la fecha límite
fecha_limite = datetime.datetime(2022, 3, 23)
diferencia = fecha_limite-fecha_nacimiento
#Se puede acceder incluso a segundos pero no se ncesita
dias_vividos = diferencia.days
#Se saca el modulo
modulo_dias = (dias_vividos%3)+1
mensaje = "El numero de dias vivido hasta el 23 de marzo del 2022 desde tu nacimiento es {} y el modulo 2 de esto es {}.".format(dias_vividos, modulo_dias)

print(mensaje)