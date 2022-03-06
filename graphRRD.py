import sys
import rrdtool
import time


def graficar(nombre, opcion, tiempo):

    nombre= nombre + ".rrd"
    tiempo_actual = int(time.time())
    # Grafica desde el tiempo actual menos diez minutos
    tiempo_inicial = tiempo_actual - int(tiempo)
    if opcion == 1:
        ret = rrdtool.graph("grafica1.png",
                    "--start", str(tiempo_inicial),
                    "--end", "N",
                    "--vertical-label=Recibidos",
                    "--title=Paquetes multicast recibidos \n Usando SNMP y RRDtools",
                    "DEF:multicast_recibidos=" + nombre + ":multicastrecibidos:AVERAGE",
                    "LINE3:multicast_recibidos#EC201B:Multicast recibidoa"
                    )
    elif opcion == 2:
        ret = rrdtool.graph("grafica2.png",
                    "--start", str(tiempo_inicial),
                    "--end", "N",
                    "--vertical-label=Segmentos",
                    "--title=Paquetes recibidos exitosamente \n Usando SNMP y RRDtools",
                    "DEF:recibidos_IPv4=" + nombre + ":recibidosIPv4:AVERAGE",
                    "LINE3:recibidos_IPv4#38EC1B:Recibidos IPv4")

    elif opcion == 3:
        ret = rrdtool.graph("grafica3.png",
                    "--start", str(tiempo_inicial),
                    "--end", "N",
                    "--vertical-label=Segmentos",
                    "--title=Mensajes de respuesta ICMP que ha enviado el agente \n Usando SNMP y RRDtools",
                    "DEF:ICMP_enviado=" + nombre + ":ICMPenviado:AVERAGE",
                    "LINE3:ICMP_enviado#1B43EC:ICMP enviados")

    elif opcion == 4:
        ret = rrdtool.graph("grafica4.png",
                    "--start", str(tiempo_inicial),
                    "--end", "N",
                    "--vertical-label=Segmentos",
                    "--title=Segmentos enviados, incluyendo los de las conexiones actuales pero excluyendo los que contienen solamente octetos retransmitidos \n Usando SNMP y RRDtools",
                    "DEF:segmentos_enviados=" + nombre + ":segmentosenviados:AVERAGE",
                    "LINE3:segmentos_enviados#EC1BE0:segmentos enviados")

    else:
        ret = rrdtool.graph("grafica5.png",
                    "--start", str(tiempo_inicial),
                    "--end", "N",
                    "--vertical-label=Segmentos",
                    "--title=Datagramas recibidos que no pudieron ser entregados por cuestiones distintas a la falta de aplicacion en el puerto destino \n Usando SNMP y RRDtools",
                    "DEF:datagramas_recibidos=" + nombre + ":datagramasrecibidos:AVERAGE",
                    "LINE3:datagramas_recibidos#000000:Datagramas recibidos")
