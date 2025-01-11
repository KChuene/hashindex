import sys
import sqlite3
import os
import core.libs.argshandler as args
from core.api import app
from core.index import Index
from core.libs.sqlhandler import SQLHandler

MODES = ["local", "public"]

def xor(opts : list[str], searchspace : list[str]):
    value, isxor = None, False

    space = set(searchspace)
    for opt in opts:
        inspace = opt in space
        if inspace and not isxor:
            value, isxor = True

        elif inspace:
            return False
        
    return value, isxor

def connectdb():
    if not os.path.exists("./dir"):
        os.mkdir("./dir")

    dbconn = sqlite3.connect("./db/hindex.db")
    qhandler = SQLHandler(dbconn)

def argsof(method : str):
    opts = {
        "-add": ["-h", "-v"],
        "-get": []
    }
    return [args.readargs(opt) for opt in opts[method]]

def main():
    method, isxor = xor(args.METHODS, sys.argv)
    if not isxor:
        args.bye(f"(!) Methods {args.METHODS} are exclusive.")
    
    methargs = argsof(method)

    hashindex = Index()
    run = {
        "-add": hashindex.add,
        "-get": hashindex.get
    } 
    run(*methargs)

if __name__=="__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"

    if not mode in MODES: 
        args.bye(f"(!) Only {MODES} modes available.")

    connectdb()
    if mode == "public":
        app.run(host="localhost", port=80, debug=True)

    else:
        main()