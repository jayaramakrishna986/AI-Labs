# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "You are Welcomed"

# @app.route("/add", methods=["POST"])
# def add_data():
#     data = request.get_json()

#     name = data.get("name")
#     age = data.get("age")

#     return jsonify({
#         "message": f"User {name} added",
#         "age": age
#     })
# get method
# @app.route("/Users",methods=["GET"])





# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask,jsonify,request

# app=Flask(__name__)

# @app.route("/")
# def Home():
#     return f"You are in the Home Welcome you"

# @app.route("/users",methods=["GET"])
# def users():
#     return jsonify({
#         "Name":"Jairam",
#         "Age":43
#     })


# @app.route("/square/<int:num1>")
# def square(num1):
#     return jsonify({
#         "Number":num1,
#         "Square of number":num1*num1
#     })
# @app.route("/add",Methods=["GET","POST"])
# def add():
#     data=request.get_json()

#     a=data.get("a")
# if __name__== "__main__":
#     app.run(debug=True)

# import requests

# url="https://jsonplaceholder.typicode.com/users"

# response=requests.get(url)

# data=response.json()

# for user in data:
#     print(user["name"],user["email"])


# import requests

# url="https://jsonplaceholder.typicode.com/users"

# responses=requests.get(url)

# data=responses.json()

# for i in data:
#     print(i["name"],i["email"])

import requests

url="https://jsonplaceholder.typicode.com/users"

data ={
    "name":"Jai ram",
    "Age":22
}

responses=requests.post(url,json=data)

print(responses.json())

data1={"name":"jaya rama krishna"}

responses=requests.put(url,json=data1)
print(responses.json())

responses=requests.delete(url)
print(responses)