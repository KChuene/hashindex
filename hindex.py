import sys
import core.libs.argshandler as args
from core.api import app

MODES = ["local", "public"]

def main():
    pass

if __name__=="__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "local"

    if not mode in MODES: 
        args.bye(f"(!) Only {MODES} modes available.")

    if mode == "public":
        app.run(host="localhost", port=80, debug=True)

    else:
        main()