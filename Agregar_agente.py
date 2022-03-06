import os
from CreateRRD import Crear_rrd

def Agregar():
    file = open("Agentes.txt", "r")
    IP= input("Introduzca la IP de agente que sera agragado:")
    Comunidad = input ("Introduzca el nombre de la comunidad:")
    with open("Agentes.txt") as myfile:
        total_agentes = sum(1 for line in myfile)
    file2 = open("noagentes.txt", "r")
    numero = int(file2.readline())
    file = open("Agentes.txt", "a")
    nombre = file.write("Agente" + str(numero + 1) + " " + IP + " " + Comunidad + os.linesep)
    file = open("Agentes.txt", "r")
    file2 = open("noagentes.txt", "w")
    file2.write(str(numero+1))
    tmp = file.readlines()[-1]
    print(tmp)
    Crear_rrd(tmp.split()[0])
    file.close()

#Agregar()