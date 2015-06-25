__author__ = 'luishoracio'
import datetime


def setPayload(id_origen=None, version=None, presion1=None, presion2=None, campo1=None, campo2=None, bateria=None, hora=None,
               dia=None):

    payload = {
        'id_valvula': getIdValvula(id_origen),
        'email': id_origen,
        'version': version, # .replace("#",":"),
        'presion1': getValorPresion(presion1),
        'presion2': getValorPresion(presion2),
        'campo1': campo1,
        'campo2': campo2,
        'bateria': bateria.replace("B:", ""),
        'hora': hora,
        'dia': dia,
        'fecha': build_fecha(dia, hora)
    }
    print payload
    return payload


def setPayloadHMB5(id_origen=None, version=None, mensaje=None):

    payload = {
        'id_origen': id_origen,
        'version': version,
        'mensaje':mensaje
    }
    print payload
    return payload


def getIdValvula(id_origen=None):
    retId = ""

    try:
        aux = id_origen.split("@")
        valor = aux[0][-1]
        retId = valor
    except Exception as ex:
        print ex

    return retId


def getValorPresion(presion=None):
    retPresion = ""

    try:
        aux = presion.split(":")
        valor = aux[1].split(" ")
        retPresion = valor[0]
    except Exception as ex:
        print ex

    return retPresion


def build_fecha(fecha=None, hora=None):
    retFecha = ""

    try:
        new_fecha = fecha.split(".")
        currentYear = datetime.datetime.now().year
        retFecha = "{}-{}-{} {}:00".format(currentYear, new_fecha[1][:-1], new_fecha[0], hora)
    except Exception as ex:
        print ex

    return retFecha