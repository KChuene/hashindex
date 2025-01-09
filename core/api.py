import json
import os
from flask import Flask, render_template

app = Flask("Hashindex", template_folder="html")

@app.route("/api", methods=["GET"])
def get():
    result = os.listdir("./")
    return json.dumps(result)

@app.route("/api", methods=["POST"])
def add():
    result = {
        "success": True,
        "message": "Added successfully!"
    }
    return json.dumps(result)

@app.route("/")
def index():
    return render_template("index.html")
