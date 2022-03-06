import os

def Borrar():
    Agente = input("Introduzca el agente que sera eliminado:")
    with open("Agentes.txt") as myfile:
        total = sum(1 for line in myfile)
    agentes_txt = open("Agentes.txt", "r")
    file = open("Agentesupdate.txt", "w")
    print(total)
    for i in range(total):
        linea_a = agentes_txt.readline()
        if linea_a.split()[0] != Agente:
            file.write(linea_a)

    agentes_txt = open("Agentes.txt", "w")
    file = open("Agentesupdate.txt", "r")
    for i in range(total):
        linea_a = file.readline()
        agentes_txt.write(linea_a)
    agentes_txt.close()
    file.close()
    archivo1=(Agente + ".rrd")
    archivo2=(Agente + ".xml")
    os.remove(archivo1)
    os.remove(archivo2)

#Borrar()