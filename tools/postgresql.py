import time
import psycopg2



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
        try:
            time.sleep(5)
            cur.execute("SELECT user_name, api_key, shop_url FROM tma.customer WHERE email='" + email + "'")
            for api_key, user_name, shop_url in cur.fetchall():
                return user_name, api_key,  shop_url
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
    conn.close()