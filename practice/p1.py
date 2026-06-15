# def add(a,b):
#     print(f"The addition of two number:{a+b}")

# def sub(a,b):
#     return (f"The subtraction of two numbers:{a-b}")


# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print( f"Your name  is {self.name} and my age is {self.age}")
    
# s1=Student("Jairam",90)
# s1.display()


# import requests

# data = {
#     "name": "Jairam",
#     "role": "AI Engineer"
# }

# response = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json=data
# )

# print(response.status_code)
# print(response.json())

from flask import Flask, jsonify

app=Flask(__name__)
@app.route("/", methods=['GET'])
def home():
    return "You are at Home!"

@app.route("/students", methods=['GET'])

def get_students():
    return jsonify({
        "Name":"jairam",
        "Age":23    
    })

app.run(debug=True)