import os
from getSNMP import consultaSNMP
from getSNMP_p import consultaSNMP_p
from Agregar_agente import Agregar
from Borrar_agente import Borrar
from Generar_reporte import Generar

def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
        string_value = bytes.fromhex(hex).decode('utf-8')
        return string_value
    return hex

def menu():
    print("Seleccione una opción")
    print("1) Agregar agente")
    print("2) Borrar agente")
    print("3) Generar reporte")
    print("4) Salir")

def principal():
    print("Información de los agentes")
    agentes_txt = open("Agentes.txt", "r")
    with open("Agentes.txt") as myfile:
        total_agentes = sum(1 for line in myfile)
    print("Numero de agentes que están en monitoreo:" + str(total_agentes))
    for n in range(total_agentes):
        datos_agente = agentes_txt.readline()
        print("Conectividad con el agente " + str(n+1) + " " + str(consultaSNMP_p(datos_agente.split()[2], datos_agente.split()[1],'1.3.6.1.2.1.1.1.0')))
        num_inter = int(consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],'1.3.6.1.2.1.2.1.0'))
        print("Numero de interfaces:", num_inter)
        print("Estado y descripción" )
        for n in range(num_inter):
            ip_d = '1.3.6.1.2.1.2.2.1.2.' + str(n+1)
            ip_e = '1.3.6.1.2.1.2.2.1.7.' + str(n + 1)
            print("Interface" + str(n+1) + ':' + str(hex_to_string(consultaSNMP_p(datos_agente.split()[2], datos_agente.split()[1],ip_d))))
            if  (int(consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],ip_e)) == 1):
                print("Activo")
            else:
                print("Inactivo")
    agentes_txt.close()
    opcion()



def opcion():
    while True:
        menu()

        opcionMenu = input("Inserte un valor: ")

        if opcionMenu == "1":
            #os.system("clear")
            print("Agregar agente")
            Agregar()
            principal()
        elif opcionMenu == "2":
            print("Borrar Agente")
            Borrar()
        elif opcionMenu == "3":
        #os.system("clear")
            Generar()
            print("Reporte generado")
        elif opcionMenu == "4":
            exit()
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
