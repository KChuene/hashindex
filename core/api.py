import json
import os
from core.index import Index
from core.libs.validator import Validator
from flask import Flask, jsonify, request, render_template

app = Flask("Hashindex", template_folder="html")
hashindex = Index() 
validator = Validator()

def respond(success : bool, message : str):
    return {
        "success": success,
        "message": message
    }

@app.route("/api", methods=["GET"])
def get():
    data = request.form.to_dict()

    isvalid = validator.all(data, {"hash"})
    if not isvalid:
        return jsonify( respond(True, "No valid data provided.") )
    
    indexout = hashindex.get(data["hash"])
    return jsonify( respond(indexout[0], indexout[1]) )

@app.route("/api", methods=["POST"])
def add():
    data = request.get_json()

    isvalid = validator.all(data, {"htype", "hash", "phrase"})
    if not isvalid:
        return jsonify( respond(False, "No valid data provided.") )

    indexout = hashindex.add(data["htype"], data["hash"], data["phrase"])
    return jsonify( respond(indexout[0], indexout[1]) )

@app.route("/")
def index():
    return render_template("index.html")