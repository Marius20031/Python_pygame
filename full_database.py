from random import random

import pymongo
from Importuri import *
from pymongo import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from asyncio import sleep
from random import random
import pygame
from Importuri import *
from runde import *
import numpy as np
from importuri_bgd import *

uri = "mongodb+srv://zenbot2020:KqVuBbkrJDuU18Ui@cluster5511.xyvvlgm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Datapygame"]
collection = db["Collection"]
# astea le vreau mereu ^
def random_guest_name():
    var=random.randint(324123,2134432)
    var+=123412
    return("Guest"+str(var))

def verificare_exisa(username,parola):
    query = {
        'username': username,
        'password': parola
    }

    var=collection.find_one(query)
    print(var)
    if var:
        return 1
    else:
        return 0

def verificare_exista_username(username):
    query = {
        'username': username,
    }

    var=collection.find_one(query)
    print(var)
    if var:
        return 1
    else:
        return 0

def login_try(username,password):
    #verific daca exista prima data, si daca nu exista inserez
    if verificare_exista(username,password)==1:
        print("Login corect, datele sunt corecte")
    else: # creeaza
        print("Datele introduse sunt gresite")

def create_try(username,password):
    #verific daca exista prima data, si daca nu exista inserez
    if verificare_exista_username(username)==1:
        print("Username deja folosit")
    else: # creeaza
        user_id = 1 # ce alege
        xp = 0
        data_to_insert = {
            'username': username,
            'password': password,
            'id': user_id,
            'xp': xp
        }
        collection.insert_one(data_to_insert)
        print("Utilizator creeat cu succes")

def adauga_xp_lovire_buna():
    query = {
        'username': username_conectat[0],
    }
    query = {
        'username': username_conectat[0],
    }
    var = collection.find_one(query)
    # filter_criteria = {'_id': 'document_id_to_update'}  # Replace 'document_id_to_update' with the actual document ID
    xp = var.get('xp')
    print(xp)
    xp += 15
    collection.update_one(query, {'$set': {'xp': xp}})
    print("ai nimerit")
def adauga_xp_ratare():
    query = {
        'username': username_conectat[0],
    }
    var = collection.find_one(query)
    #filter_criteria = {'_id': 'document_id_to_update'}  # Replace 'document_id_to_update' with the actual document ID
    xp=var.get('xp')
    print(xp)
    xp+=5
    collection.update_one(query, {'$set': {'xp': xp}})
    print("ai ratat")
#def level: