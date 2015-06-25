# -*- coding: utf-8 -*-
__author__ = 'luishoracio'
import requests
import poplib
from email import parser
from time import sleep

difference = 50
rangeLow = 9665 
rangeHigh = rangeLow + difference

while True:

    pop_conn = poplib.POP3('mail.basipesa.com')
    pop_conn.user('hmb@basipesa.com')
    pop_conn.pass_('250215hmb')

    print "{} - {}".format(pop_conn.stat(), len(pop_conn.list()[1]))
    totalMessages = int(pop_conn.stat()[0])
    pop_conn.quit()

    print "{}".format(totalMessages)

    limit = totalMessages

    boolError = False
    boolDouble = False

    while rangeLow < limit:
        if rangeHigh > limit:
            rangeHigh = limit
        print "{} - {} - {}".format(rangeLow, rangeHigh, limit)
        pop_conn = poplib.POP3('mail.basipesa.com')
        pop_conn.user('hmb@basipesa.com')
        pop_conn.pass_('250215hmb')
        pop_conn.set_debuglevel(1)

        boolError = False
        try:
            messages = [pop_conn.retr(i) for i in range(rangeLow, rangeHigh)] # len(pop_conn.list()[1]) + 1)]
            # Concat message pieces:
            messages = ["\n".join(mssg[1]) for mssg in messages]
            #Parse message into an email object:
            messages = [parser.Parser().parsestr(mssg) for mssg in messages]
            for message in messages:
                test = message.get_payload().rstrip('\r\n')
                origin = message['from'].replace("<", "").replace(">", "")
                version = message['subject'].replace("=?UTF-8?Q?", "").replace("?=", "").replace("_", " ")
                print "{} - {} - {}".format(origin, version, test)
                payload = {'id_origen': origin, 'version': version, 'mensaje': test}
                r = requests.get("http://hidromedidores.com.mx/jmas/api/insertarCola.php", params=payload)
                print "{} {}".format(r.text, r.status_code)

        except Exception as ex:
            boolError = True
            print ex
            print i

        pop_conn.quit()

        if not boolError:
            if boolDouble:
                rangeLow = rangeHigh + 1
                rangeHigh = rangeLow + difference
                boolDouble = False
            else:
                if i == rangeLow:
                    rangeLow += difference
                    rangeHigh += difference
                    boolDouble = False
                else:
                    rangeLow = i + 1
                    rangeHigh = rangeLow + difference
                    boolDouble = False
        else:
            boolDouble = True
            rangeHigh = i

    print "Last read - {}".format(rangeLow)
    sleep(5)