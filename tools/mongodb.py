import datetime
import configparser
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

config = configparser.RawConfigParser()
config.read('../conf.ini')
print(config.get('MongoDB', 'host'))
client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=10, connectTimeoutMS=20000)
db = client.triggmine


def check_mongodb_connection():
    try:
        client.server_info()
    except ServerSelectionTimeoutError or ServerSelectionTimeoutError:
        raise Exception('Error connection to MongoDB')


def mongodb_insert_user(email, name, password, industry, shop, api_key, user_name, shop_currency):
    check_mongodb_connection()
    collection = db.users
    collection.save({
        "email": email,
        "name": name,
        "password": password,
        "industry": industry,
        "shop": shop,
        "date": datetime.datetime.now(),
        "api_key": api_key,
        "user_name": user_name,
        "shop_currency": shop_currency})


def mongodb_last_user(data='email'):
    check_mongodb_connection()
    collection = db.users
    if data == 'email':
        for email in collection.find({"date": {"$lte": datetime.datetime.now()}}).sort([('date', -1)]).limit(1):
            print(email['email'])
            return email['email']
    elif data == 'api_key':
        for api_key in collection.find({"date": {"$lte": datetime.datetime.now()}}).sort([('date', -1)]).limit(1):
            return api_key['api_key']
    elif data == 'user_name':
        for user_name in collection.find({"date": {"$lte": datetime.datetime.now()}}).sort([('date', -1)]).limit(1):
            return user_name['user_name']

print(mongodb_last_user(data='user_name'))
