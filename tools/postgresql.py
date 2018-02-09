import time
import configparser
import psycopg2
from data.users import NEW_USER_EMAIL
from tools.mongodb import mongodb_last_user

config = configparser.ConfigParser()
config.read('../conf.ini')
config.get('Sql', 'user')


conn = psycopg2.connect(dbname=config.get('Sql', 'dbname'),
                        user=config.get('Sql', 'user'),
                        password=config.get('Sql', 'password'),
                        host=config.get('Sql', 'host'))


def check_pg_connection():
    try:
        conn
    except psycopg2.OperationalError:
        raise Exception('Error connection to PostgreSQL')
    finally:
        conn.close()


def get_user_data(email):
    cur = conn.cursor()
    for i in range(1):
        time.sleep(0.5)
        try:
            cur.execute("SELECT user_name, api_key, shop_url, shop_currency, first_name, esp_email_from, support_email "
                        "FROM tma.customer  "
                        "WHERE email='" + email + "'")
            for user_name, api_key, shop_url, shop_currency, first_name, esp_email_from, support_email in cur.fetchall():
                return user_name, api_key,  shop_url, shop_currency, first_name, esp_email_from, support_email
        except:
            break
    else:
        raise Exception('Email ' + email + ' do nof fiend in DB')
    conn.close()


def activate_setup_trial_modal(user_name):
    cur = conn.cursor()
    sql = """UPDATE """ + user_name + """."control_customerMetadata" SET "Value"='true' 
                WHERE "Key"='isWelcomeModalShown'"""
    cur.execute(sql)
    conn.commit()


def set_currency(user_name, currency='USD'):
    cur = conn.cursor()
    sql = "UPDATE tma.customer SET shop_currency=(%s) WHERE user_name=(%s)"
    data = (currency, user_name)
    cur.execute(sql, data)
    conn.commit()


def set_logo_image(user_name, image='https://s3-eu-west-1.amazonaws.com/tgmimages/cabinet481014452/'
                                    'f6a70d31-2718-413c-81d2-35223ba01d47'):
    cur = conn.cursor()
    sql = "UPDATE tma.customer SET logo_url=(%s) WHERE user_name=(%s)"
    data = (image, user_name)
    cur.execute(sql, data)
    conn.commit()


def set_support_email(user_name, email=NEW_USER_EMAIL):
    cur = conn.cursor()
    sql = "UPDATE tma.customer SET support_email=(%s) WHERE user_name=(%s)"
    data = (email, user_name)
    cur.execute(sql, data)
    conn.commit()


def select_user_industry(email):
    cur = conn.cursor()
    time.sleep(0.3)
    cur.execute("SELECT industry_uid FROM tma.customer WHERE email=(%s)", (email,))
    for industry_uid in cur.fetchone():
        return industry_uid
    conn.close()


def delete_plugin_integration():
    cur = conn.cursor()
    sql = "DELETE from {0}.react_plugin_diagnostic".format(mongodb_last_user(data='user_name'))
    data = mongodb_last_user('user_name')
    cur.execute(sql, data)
    conn.commit()
    conn.close()