import sys
import sqlite3
import core.libs.argshandler as args
from core.api import app
from core.libs.sqlhandler import SQLHandler

MODES = ["local", "public"]

def main():
    dbconn = sqlite3.connect("db/hindex.db")
    sqlh = SQLHandler(dbconn)

if __name__=="__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"

    if not mode in MODES: 
        args.bye(f"(!) Only {MODES} modes available.")

    if mode == "public":
        app.run(host="localhost", port=80, debug=True)

    else:
        main()