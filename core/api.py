import json
import os
from flask import Flask, jsonify, render_template

app = Flask("Hashindex", template_folder="html")

@app.route("/api", methods=["GET"])
def get():
    result = os.listdir("./")
    return jsonify(result)

@app.route("/api", methods=["POST"])
def add():
    
    result = {
        "success": True,
        "message": "Added successfully!"
    }
    return jsonify(result)

@app.route("/")
def index():
    return render_template("index.html")
