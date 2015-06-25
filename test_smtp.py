__author__ = 'luishoracio'
import smtplib
import string
import requests
import Models
import Utils

cola_list = []
r = requests.get("http://hidromedidores.com.mx/jmas/api/getMensajes.php").json()

for cola in r:
    cola_list.append(Models.Mensajes(
        cola['id_mensaje'],
        cola['usuario'],
        cola['email_destino'],
        cola['mensaje'],
    ))

for tupla in cola_list:

    SUBJECT = tupla.mensaje
    TO = "Valvula <{}>".format(tupla.email_destino)
    FROM = "basi <hmb@basipesa.com>"
    text = "HMB 5.0"
    BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text), "\r\n")

    # server = smtplib.SMTP_SSL('smtp.basipesa.com', 587, timeout=10)
    server = smtplib.SMTP('smtp.basipesa.com', 587)
    # server.connect() # "smtp.gmail.com", "submission")
    server.starttls()
    server.ehlo()
    server.login('hmb@basipesa.com', '250215hmb')
    server.set_debuglevel(1)
    server.sendmail(FROM, TO, BODY)
    server.quit()