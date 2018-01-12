import imaplib
import quopri
import re
import time


def check_email(sub):
    for i in range(30):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login('automation.test.tg@gmail.com', 'filosof0955567051')
            mail.select("INBOX")
            result, data = mail.uid('search',  None, '(UNSEEN)', '(HEADER Subject "' + sub + '")')
            ids = data[0]  # Получаем сроку номеров писем
            id_list = ids.split()  # Разделяем ID писем
            if not id_list:
                time.sleep(10)
                continue
            else:
                pass
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
            else:
                continue
        except:
            raise Exception('Email incorrect')