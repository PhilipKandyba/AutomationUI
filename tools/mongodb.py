import datetime
import pytest
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=10, connectTimeoutMS=20000)
db = client.triggmine


def check_mongodb_connection():
    try:
        client.server_info()
    except ServerSelectionTimeoutError:
        raise Exception('Error connection to MongoDB')


def mongodb_insert_user(email, name, password, industry, shop):
    collection = db.users
    collection.save({
        "email": email,
        "name": name,
        "password": password,
        "industry": industry,
        "shop": shop,
        "date": datetime.datetime.now()})


def mongodb_last_user():
    check_mongodb_connection()
    collection = db.users
    for email in collection.find({"date": {"$lte": datetime.datetime.now()}}).sort([('date', -1)]).limit(1):
        return email['email']
