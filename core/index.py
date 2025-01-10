import sys
import hashlib
import libs.qstrings as qr
from libs.sqlhandler import SQLHandler



def add(hash : str, phrase : str, htype : str):
    if not htype in hashlib.algorithms_available:
        return False, "Algorithm not supported."
    
    method = getattr(hashlib, htype)
    rehash = method(phrase.encode()).hexdigest()

    if rehash != hash:
        return False, "Hash does not match phrase."
    
    query = """
        INSERT INTO Rainbow (hash, phrase)
        VALUES (?, ?);
    """
    added = sqlh.write(query, [hash, phrase])
    return True, "Added."
    
def get(hash : str):
    pass

def createtable():
    pass

def createindex():
    query = qr.CREATE_INDEX
    sqlh.write(query,)
