import sys
import hashlib
from sqlhandler import SQLHandler as sqlh

OPTIONS = ["-add", "-get", "-htype"]

def bye(message : str = "Bye bye!", show_usage : bool = True):
    print(message)
    if show_usage:
        print("usage: hindex.py [-add <hash> <value> | -get <hash>] <")

    sys.exit()

def readargs(opt : str, args : list[str], required=True, isbool : bool = False, isnum : bool = False):
    if not opt in args:
        if required:
            bye(f"(!) Option {opt} is required.")
        else:
            return None

    elif isbool:
        return True
    
    indexof = args.index(opt)
    if indexof >= len(args)-1:
        bye(f"(!) Value expected for option {opt}.")
    
    valueof = args[indexof + 1]
    if isnum and valueof.isnumeric():
        return float(valueof)
    
    elif isnum:
        bye(f"(!) Number expected for option {opt}.")

    return valueof

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

