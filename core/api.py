import json
import os
from core.index import Index
from flask import Flask, jsonify, request, render_template

app = Flask("Hashindex", template_folder="html")
hashindex = Index() 

def respond(success : bool, message : str):
    return {
        "success": success,
        "message": message
    }

def isvalid(method : str, data):
    vdator = {
        "add": type(data) is dict and {"htype", "hash", "phrase"}.issubset(data),
        "get": type(data) is dict and "hash" in data 
    }
    return vdator[method]

@app.route("/api", methods=["GET"])
def get():
    data = request.form.to_dict()
    if not isvalid("get", data):
        return jsonify( respond(True, "No valid data provided.") )
    
    indexout = hashindex.get(data["hash"])
    return jsonify( respond(indexout[0], indexout[1]) )

@app.route("/api", methods=["POST"])
def add():
    data = request.get_json()

    if not isvalid("add", data):
        return jsonify( respond(True, "No valid data provided.") )

    indexout = hashindex.add(data["htype"], data["hash"], data["phrase"])
    return jsonify( respond(indexout[0], indexout[1]) )

@app.route("/")
def index():
    return render_template("index.html")