import imaplib
import quopri
import re
import time
from selenium import webdriver

def check_email(sub):
    time.sleep(5)
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('***', '***')
    mail.select("inbox")
    for i in range(30):
        try:
            result, data = mail.uid('search', None, '(HEADER Subject "' + sub + '")')
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
            time.sleep(10)
    else:
        raise Exception('Email was not found')


webdriver.Chrome().get(check_email('Activate your account at TriggMine'))
