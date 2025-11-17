from pymongo import MongoClient
import config

# MongoDB Connection
vickdb = MongoClient(config.MONGO_URL)
vick = vickdb["VickDb"]["Vick"]

# Import internal modules
from .chats import *
from .users import *
