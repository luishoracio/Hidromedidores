# -*- coding: utf-8 -*-
__author__ = 'luishoracio'
import requests
import Models
import Utils
from time import sleep
rangeLow = 37792

while True:

    cola_list = []
    url = "http://hidromedidores.com.mx/jmas/api/getCola.php?limit={}".format(rangeLow)
    r = requests.get(url).json()

    for cola in r:
        cola_list.append(Models.Cola(
            cola['id_test'],
            cola['id_origen'],
            cola['version'],
            cola['mensaje'],
        ))

    for tupla in cola_list:
        rangeLow = tupla.id_test
        auxiliar = tupla.mensaje
        parametros = auxiliar.split(",")

        if len(parametros) > 1:
            print tupla.version
            if tupla.version == "JCAS_prueba#4":
                payload = Utils.setPayload(tupla.id_origen, tupla.version, parametros[0], parametros[1], parametros[2],
                                           parametros[3], parametros[4], parametros[5], parametros[6])
                # r = requests.get("http://hidromedidores.com.mx/jmas/api/insertarValorValvula.php", params=payload)
                # print "{} {}".format(r.text, r.status_code)
                # print parametros
            else:
                tupla.version = "HMB 5.0"
                payload = Utils.setPayloadHMB5(tupla.id_origen, tupla.version, auxiliar)

                r = requests.get("http://hidromedidores.com.mx/jmas/api/insertarValorValvulaHMB5.php", params=payload)
                print "{} {}".format(r.text, r.status_code)

    print "ULTIMO LEÍDO - {}".format(rangeLow)
    sleep(5)

# {"id_test":"1",
# "id_origen":"gprsv1@basipesa.com",
# "version":"JCAS_prueba#4",
# "mensaje":"P1:7.03 kg.cm,P2:0.70 kg.cm,,,B:13.3,06:14,16.01;"}

# {"id_test":"2",
# "id_origen":"",
# "version":"=?UTF-8?Q?HMB_5.0?=",
# "mensaje":"P1,0.00,kg.cm,P2,0.00,kg.cm,L0,F0,c1,B,11.2,09:43,04.05.15,v* 09:43 04.05.15"}