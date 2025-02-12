import sys
import sqlite3
import os
import core.libs.argshandler as args
from core.api import app
from core.index import Index
from core.libs.sqlhandler import SQLHandler

MODES = ["local", "public"]

def debugger(cindex : int):
    argstr = [
        "local -add -htype sha256 -hash 59f46bb90cffb0ed7c7e5db58bb300f3bcd714f51ae723ed91b06a3e13d4d5b6 -v p@55w0rd",
        "local -get -hash 59f46bb90cffb0ed7c7e5db58bb300f3bcd714f51ae723ed91b06a3e13d4d5b6",
        "local -add -htype sha256 -hash 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601 -v Password123",
        "local -get -hash 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601",
        "public"
    ]

    arglst = argstr[cindex].split(" ")
    for arg in arglst:
        sys.argv.append(arg)

def xor(opts : list[str], searchspace : list[str]):
    value, isxor = None, False

    space = set(searchspace)
    for opt in opts:
        inspace = opt in space
        if inspace and not isxor:
            value, isxor = opt, True

        elif inspace:
            return False
        
    return value, isxor

def argsof(method : str):
    opts = {
        # Strict Order - Matching index.function signature
        "-add": ["-htype", "-hash", "-v"], 
        "-get": ["-hash"]
    }
    return [args.readargs(opt, sys.argv) for opt in opts[method]]

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

    output = run[method](*methargs)
    print(output)

if __name__=="__main__":
    #debugger(4)
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"

    if not mode in MODES: 
        args.bye(f"(!) Only {MODES} modes available.")

    if mode == "public":
        app.run(host="localhost", port=80, debug=True)

    else:
        main()