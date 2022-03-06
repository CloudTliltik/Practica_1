#!/usr/bin/env python

import rrdtool

def Crear_rrd(Nombre):
    ret = rrdtool.create(Nombre + ".rrd",
                     "--start",'N',  # N significa ahora
                     "--step",'60',  # Definir el tiempo de step
                     "DS:multicastrecibidos:COUNTER:120:U:U",  #Paquetes multicast que ha recibido una intefaz
                     "DS:recibidosIPv4:COUNTER:120:U:U",  # Paquetes recibidos exitosamente, entregados a protocolos IPv4
                     "DS:ICMPenviado:COUNTER:120:U:U",  #Mensajes de respuesta ICMP que ha enviado el agente
                     "DS:segmentosenviados:COUNTER:120:U:U",  #Segmentos enviados, incluyendo los de las conexiones actuales pero excluyendo los que contienen solamente octetos retransmitidos
                     "DS:datagramasrecibidos:COUNTER:120:U:U",  # Datagramas recibidos que no pudieron ser entregados por cuestiones distintas a la falta de aplicacion en el puerto destino
                     "RRA:AVERAGE:0.5:1:100",
                     "RRA:AVERAGE:0.5:1:100",
                     "RRA:AVERAGE:0.5:1:100",
                     "RRA:AVERAGE:0.5:1:100",
                     "RRA:AVERAGE:0.5:1:100")#80 o 100 filas para la practica

    if ret:
        print (rrdtool.error())