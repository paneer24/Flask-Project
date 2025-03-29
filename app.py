from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()
MONGO_DB_URI =os.getenv("MONGO_DB_URI")

app = Flask(__name__)


client = MongoClient(MONGO_DB_URI)
db = client["mydatabase"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def index():
    error_message = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            error_message = "Both fields are required!"
        else:
            try:
                collection.insert_one({"name": name, "email": email})
                return redirect(url_for("success"))
            except Exception as e:
                error_message = f"Error: {str(e)}"

    return render_template("index.html", error=error_message)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
