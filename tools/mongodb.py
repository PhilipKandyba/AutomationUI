import datetime
from pymongo import MongoClient


def mongodb_insert_user(email, name, password, industry, shop):
    client = MongoClient()
    db = client.triggmine
    collection = db.users
    collection.save({
        "email": email,
        "name": name,
        "password": password,
        "industry": industry,
        "shop": shop,
        "date": datetime.datetime.now()})
