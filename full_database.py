
import hashlib
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
from Functii import *

from runde import *

uri = "mongodb+srv://zenbot2020:KqVuBbkrJDuU18Ui@cluster5511.xyvvlgm.mongodb.net/?retryWrites=true&w=majority"
#uri = "mongodb+srv://bodo2003:eoXq7eK98PQyfwsm@cluster0.facrcqq.mongodb.net/?retryWrites=true&w=majority"
#uri = "mongodb+srv://robert:LnKSGSt39JNt_@cluster0.facrcqq.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Datapygame"]
collection = db["Collection"]
def get_leaderboard():
    nr_playeri[0]=collection.count_documents({})
    var_documente=collection.find({}).sort("xp", -1)
    for document in var_documente:
        username = document.get("username")
        xp = str(document.get("xp"))
        level =str(int(int(xp)/10))

        matrice_leaderboard.append([username, level, xp])
    print(matrice_leaderboard)


# astea le vreau mereu ^
def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash

def random_guest_name():
    var=random.randint(123,912)
    var+=87
    return("Guest"+str(var))

def verificare_exisa(username,parola):
    #hashed_password = calculate_sha256(parola)
    query = {
        'username': username,
        'password_hash': parola
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
    hashed_password = calculate_sha256(password)
    if verificare_exisa(username,hashed_password)==1:
        get_leaderboard()
        print("Login corect, datele sunt corecte")
        return 0
    else: # creeaza
        print("Datele introduse sunt gresite")
        return 1

def create_try(username,password):
    #verific daca exista prima data, si daca nu exista inserez
    if verificare_exista_username(username)==1:
        print("Username deja folosit")
        return 1
    else: # creeaza
        hashed_password = calculate_sha256(password)
        user_id = 1 # ce alege
        xp = 0
        data_to_insert = {
            'username': username,
            'password_hash': hashed_password,
            'id': user_id,
            'xp': xp
        }
        collection.insert_one(data_to_insert)
        print("Utilizator creeat cu succes")
        return 0
def get_lvl():
    query = {
        'username': username_conectat[0],
    }
    var = collection.find_one(query)
    return str(int(int(var.get('xp'))/10))
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