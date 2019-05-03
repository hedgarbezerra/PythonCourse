from pymongo import MongoClient
import datetime
import pprint


class Connect:

    try:
        client = MongoClient('mongodb://localhost:27017/')
        print("Connected")

    except:
        print("Unable to contact server")

    def conTU(self):

        db = self.client.Teste
        coll = db.ProjetoTU
        return coll

    def condb(self):
        return self.client

    def getstorage(self):
        db = self.client.Teste.Storage
        return db

    def getuser(self):
        db = self.client.Teste.Usuario
        return db