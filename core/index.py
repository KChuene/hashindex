import sys
import hashlib
import core.libs.qstrings as qr
from core.libs.sqlhandler import SQLHandler

def singleton(Class):
    instances = {}

    def createdb(query : str):
        qhandler = SQLHandler(None)
        qhandler.write(query)

    def getinstance(*args):
        if not Class in instances:
            instances[Class] = Class(*args)

            createdb(qr.CREATE_TABLE)
            createdb(qr.CREATE_INDEX)
        return instances[Class]

    return getinstance

@singleton
class Index:
    def add(self, htype : str, hash : str, phrase : str):
        if not htype in hashlib.algorithms_guaranteed:
            return False, "Algorithm not supported."
        
        method = getattr(hashlib, htype)
        rehash = method(phrase.encode()).hexdigest()

        if rehash != hash:
            return False, "Hash does not match phrase."

        qhandler = SQLHandler(None)
        qhandler.write(qr.INSERT, [hash, phrase])
        return True, "Added."
    
    def get(self, hash : str):
        pass