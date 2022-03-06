from graphRRD import graficar
import time
from reportlab.pdfgen import canvas
from getSNMP import consultaSNMP
from getSNMP_p import consultaSNMP_p


def Generar():
    Agente = input("¿Cuál es el agente que será gráficado? ")
    tiempo = input("¿Cuál será el tiempo de graficación(en segundos)?")
    #Agente = "Agente1"
    for i in range(5):
        graficar("Agente1", i, tiempo)
    c = canvas.Canvas("Reporte.pdf")
    c.setFont('Helvetica', 20)
    c.drawString(25, 825, "Reporte de monitoreo")
    #Aquí se verán los datos del agente
    c.setFont('Helvetica', 12)
    with open("Agentes.txt") as myfile:
        total = sum(1 for line in myfile)
    agentes_txt = open("Agentes.txt", "r")

    for i in range(total):
        linea_a = agentes_txt.readline()
        opr = str(consultaSNMP_p(linea_a.split()[2], linea_a.split()[1], '1.3.6.1.2.1.1.1.0'))
        if linea_a.split()[0] == Agente:
            if opr.split()[0] == "Linux":
                c.drawImage('img.png', 50, 600 , 480, 200)
            else:
                c.drawImage('windos.png', 50, 600, 480, 200)
            c.drawString(25, 550, str(consultaSNMP_p(linea_a.split()[2], linea_a.split()[1], '1.3.6.1.2.1.1.1.0')))
            c.drawString(25, 500, "Escom-IPN")
            c.drawString(25, 450, "Número de interfaces" + str(consultaSNMP(linea_a.split()[2], linea_a.split()[1],'1.3.6.1.2.1.2.1.0')))
            #Tiempo de actividad
            c.drawString(25, 400, "Tiempo de actividad: " + str(
                consultaSNMP(linea_a.split()[2], linea_a.split()[1], '1.3.6.1.2.1.1.3.0')) + "segundos")
            c.drawString(25, 350, "Comunidad: " +  linea_a.split()[2])
            c.drawString(25, 300, "IP: " + linea_a.split()[1])

    # Insertamos las imagenes de las gráficas
    c.showPage()
    c.drawImage('grafica1.png', 25, 480, 480, 270)
    c.drawImage("grafica2.png", 25, 150, 480, 270)
    c.showPage()
    c.drawImage('grafica3.png', 25, 480, 480, 270)
    c.drawImage("grafica4.png", 25, 150, 480, 270)
    c.showPage()
    c.drawImage('grafica5.png', 25, 480, 480, 270)
    c.save()


#Generar()
