from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
MONGO_DB_URI = "your_mongo_connection_string"
client = MongoClient(MONGO_DB_URI)
db = client["todo_db"]
collection = db["todo_items"]

# Route to submit To-Do item
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json
    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Both fields are required"}), 400

    collection.insert_one({"name": item_name, "description": item_description})
    return jsonify({"message": "To-Do item added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
