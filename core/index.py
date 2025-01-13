import hashlib
import os
import sqlite3
import core.libs.qstrings as qr
from core.libs.sqlhandler import SQLHandler

def singleton(Class):
    instances = {}

    def connectdb():
        if not os.path.exists("./db"):
            os.mkdir("./db")

        dbconn = sqlite3.connect("./db/hindex.db")
        return SQLHandler(dbconn)

    def createdb(query : str, qhandler : SQLHandler):
        qhandler.write(query)

    def getinstance():
        qhandler = connectdb()

        if not Class in instances:
            instances[Class] = Class(qhandler)

            createdb(qr.CREATE_TABLE, qhandler)
            createdb(qr.CREATE_INDEX, qhandler)
        return instances[Class]

    return getinstance

@singleton
class Index:
    def __init__(self, qhandler : SQLHandler):
        self.qhandler = qhandler

    def add(self, htype : str, hash : str, phrase : str):
        if not htype in hashlib.algorithms_guaranteed:
            return False, "Algorithm not supported."
        
        method = getattr(hashlib, htype)
        rehash = method(phrase.encode()).hexdigest()

        if rehash != hash:
            return False, "Hash does not match phrase."

        self.qhandler.write(qr.INSERT, (hash, phrase,))
        return True, "Added."
    
    def get(self, hash : str):
        result = self.qhandler.read(qr.SELECT, (hash,))

        if result and len(result[0]) >= 2:
            return True, {
                "hash": result[0][0],
                "phrase": result[0][1]
            }
        
        return False, "Nothing."