# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/")
# def home():
#     return f"You are Welcome!!!"

# @app.get("/users")
# def Users():
#     return ["Jairam","Krishna","H1","98"]

# @app.post("/add_user")
# def add_user(name :str):
#     return f"message is added into the script{str}"
# from fastapi import FastAPI

# app=FastAPI()

# students=[]
# @app.get("/")
# def Home():
#     return f"You are at Home"

# @app.get("/Students1")
# def student():
#     return students

# @app.post("/students")
# def add_student(name:str):
#     students.append(name)
#     return students


#challange

from fastapi import FastAPI

app=FastAPI()
students=[]

@app.get("/")
def Home():
    return "You are at Home"

@app.post("/addstudent")
def add_student(id:int,name:str,age:int):
    student={
        "id":id,
        "name":name,
        "age":age
    }
    students.append(student)
    return f"Student added {student}"

@app.get("/student")
def display():
    return students
