from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Flask + Docker!"

@app.route("/ping")
def ping():
    mongo_host = os.environ.get("MONGO_HOST", "localhost")
    client = MongoClient(f"mongodb://{mongo_host}:27017", serverSelectionTimeoutMS=2000)
    try:
        client.admin.command("ping")
        return "MongoDB connexion OK"
    except Exception as e:
        return f"MongoDB connexion FAIL: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
