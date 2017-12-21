import imaplib
import quopri
import re
import time


def check_email(sub):
    time.sleep(10)
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('philip.kanduba', 'filosof0955567051')
    mail.select("inbox")
    for i in range(30):
        try:
            result, data = mail.uid('search', None, '(UNSEEN)', '(HEADER Subject "' + sub + '")')
            ids = data[0]  # Получаем сроку номеров писем
            id_list = ids.split()  # Разделяем ID писем
            latest_email_uid = data[0].split()[-1]  # Берем последний ID
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            utf8_email = raw_email.decode('utf-8')
            decode_email = str(quopri.decodestring(utf8_email))
            str_decode_email = str(decode_email)
            if len(str_decode_email) > 0:
                r = re.search('http://email([^"]|"")*', str_decode_email).group(0)
                print(r)
                return r
                break
        except:
            print(i)
            time.sleep(3)
    else:
        raise Exception('Email was not found')
