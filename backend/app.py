from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/users", methods=["GET"])
def get_users():
    users = list(mongo.db.users.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Campos 'name' e 'email' são obrigatórios."}), 400
    mongo.db.users.insert_one({"name": name, "email": email})
    return jsonify({"message": f"Usuário {name} adicionado com sucesso!"}), 201

@app.route("/api/users/<name>", methods=["DELETE"])
def delete_user(name):
    result = mongo.db.users.delete_one({"name": name})
    if result.deleted_count == 0:
        return jsonify({"error": "Usuário não encontrado."}), 404
    return jsonify({"message": f"Usuário {name} removido com sucesso."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
