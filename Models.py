__author__ = 'luishoracio'

class Cola:
    id_test = None
    id_origen = None
    version = None
    mensaje = None

    def __init__(self, id_test = None, id_origen = None, version_msg = None, mensaje = None):
        self.id_test = id_test
        self.id_origen = id_origen
        self.version = version_msg
        self.mensaje = mensaje

class Mensajes:
    id_mensaje = None
    usuario = None
    email_destino = None
    mensaje = None

    def __init__(self, id_mensaje = None, usuario = None, email_destino = None, mensaje = None):
        self.id_mensaje = id_mensaje
        self.usuario = usuario
        self.email_destino = email_destino
        self.mensaje = mensaje