import os
os.system("pip install requests")
os.system("pip install flask")
os.system("pip install threading")
import requests
from flask import Flask, jsonify, request
from threading import Thread

app = Flask('')


@app.route("/")
def main():
  return jsonify({"status": "up"})

@app.route("/api")
def handler():
    try:
        get = request.args.get('endpoint')
        url = f"https://api.scratch.mit.edu{get}"

        json = requests.get(url)
        json = json.json()
        return jsonify(json)
    except:
        return jsonify({"code": "ResourceNotFound"})

@app.route("/html")
def html():
    try:
        get = request.args.get('endpoint')

        json = requests.get(f"https://scratch.mit.edu{get}")

        json = json.text
        return json

    except:
        return jsonify({"code": "ResourceNotFound"})


def run():
    app.run(host="0.0.0.0", port=9999)


server = Thread(target=run)
server.start()
