from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "You are Welcomed"

@app.route("/add", methods=["POST"])
def add_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return jsonify({
        "message": f"User {name} added",
        "age": age
    })
# get method
# @app.route("/Users",methods=["GET"])





if __name__ == "__main__":
    app.run(debug=True)