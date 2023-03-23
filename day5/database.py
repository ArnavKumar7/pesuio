from pymongo import MongoClient
import settings

client = MongoClient(settings.mongo_uri, settings.port)
db = client.pesuioteam
