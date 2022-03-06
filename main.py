from Menu import principal
from CreateRRD import Crear_rrd
import threading


def Prim_cre():
    file = open("Agentes.txt", "r")
    with open("Agentes.txt") as myfile:
        total_agentes = sum(1 for line in myfile)
    for i in range(total_agentes):
        ar = file.readline()
        Crear_rrd(ar.split()[0])

def main():

    #Prim_cre()
    principal()


main()