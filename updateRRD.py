import time
import rrdtool
from getSNMP import consultaSNMP

#def update():
while 1:
    try:
        agentes_txt = open("Agentes.txt", "r")
        with open("Agentes.txt") as myfile:
            total_agentes = sum(1 for line in myfile)
        for n in range(total_agentes):
            datos_agente = agentes_txt.readline()
            packmulti_in = int(
            consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],
                         '1.3.6.1.2.1.2.2.1.12.2'))  # Paquetes multicast que ha recibido una intefaz
            packIP4v = int(
            consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],
                         '1.3.6.1.2.1.4.3.0'))  # Paquetes recibidos exitosamente, entregados a protocolos IPv4
            ICMP_echo = int(
            consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],  # Echo, Timestamp, address mask
                         '1.3.6.1.2.1.5.22.0'))  # Mensajes de respuesta ICMP que ha enviado el agente
            segmentos_enviados = int(
            consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],
                         '1.3.6.1.2.1.6.11.0'))  # Segmentos enviados, incluyendo los de las conexiones actuales pero excluyendo los que contienen solamente octetos retransmitidos
            datagramas_recibidos = int(
            consultaSNMP(datos_agente.split()[2], datos_agente.split()[1],
                         '1.3.6.1.2.1.7.3.0'))  # Datagramas recibidos que no pudieron ser entregados por cuestiones distintas a la falta de aplicacion en el puerto destino

            valor = "N:" + str(packmulti_in) + ':' + str(packIP4v) + ':' + str(ICMP_echo) + ':' + str(
            segmentos_enviados) + ':' + str(datagramas_recibidos)
            print(datos_agente.split()[0] + valor)
            rrdtool.update(datos_agente.split()[0] + ".rrd", valor)
            rrdtool.dump(datos_agente.split()[0] + ".rrd", datos_agente.split()[0] + ".xml")
    except:
        print("No se encontró algún archivo")
    finally:
        agentes_txt.close()
        time.sleep(1)


if ret:
    print(rrdtool.error())
    time.sleep(300)
