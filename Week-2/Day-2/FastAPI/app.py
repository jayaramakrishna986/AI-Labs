# from fastapi import FastAPI
# from fastapi import HTTPException

# app=FastAPI()

# students=[]

# @app.get("/")
# def Home():
#     return f"You are at Home!!!"

# @app.post("/addstudent")
# def add_student(id:int,name :str,age:int):
#     student={
#         "id":id,
#         "name":name,
#         "age":age
#     }
#     students.append(student)

# @app.get("/students")
# def display():
#     return students


# @app.get("/students/{id1}")
# def get_student(id1:int):
#     for i in students:
#         if i["id"]==id1:
#             return i
#     raise HTTPException(status_code=404,detail="Student not found")


# @app.delete("/students/{id1}")
# def delete_student(id1: int):
#     for i in students:
#         if i["id"] == id1:
#             students.remove(i)
#     raise HTTPException(status_code=404, detail="Student not found")

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel,Field
from typing import List,Optional

app=FastAPI()

# class Product():
#     id:int
#     name : str=Field(...,min_length=3,max_length=50)
#     price:float=Field(...,gt=0)
#     in_stock:bool = True
#     categorgy:Optional[str]=None
class Product():
    id :int
    name:str=Field(...,min_length=3,max_length=50)
    price:float=Field(...,gt=0)
    in_stock:bool=True
    categprgy:Optional[List]=None

products=[]

@app.get("/")
def home():
    return f"You are in Home"

@app.post("/product/add_product")
def addproduct(pid:int,p_name:str,price:int):
    product={
        "pid":pid,
        "p_name":p_name,
        "price":price
    }
    products.append(product)

@app.get("/product")
def product():
    return products

@app.get("/product1/{p_id}")
def find_pid(p_id:int):
    for i in products:
        if i["pid"]==p_id:
            return i 
    raise HTTPException(status_code=404,detail="Product not found")

@app.delete("/product/{p_id}")
def delete_item(p_id:int):
    for i in products:
        if i["p_id"]==p_id:
            products.remove(i) 
    raise Exception(status_code=404,detail="Product not found")


# Query paramaters
@app.get("/products")
def get_products(catgeory:str,price:int):
    print(f"Category:{catgeory} and Price {price}" )


# students = []

# for i in range(1, 101):
#     students.append({
#         "id": i,
#         "name": f"Student{i}",
#         "age": 18 + (i % 5)
#     })


# @app.get("/students")
# def get_students(skip :int =0,limit:int =10):
#     return students[skip:skip+limit]


from pydantic import Field
from pydantic import BaseModel

students=[]
class Student(BaseModel):
    name:str=Field(...,min_length=3)
    age:int=Field(...,gt=0,lt=100)
    id:int=Field(...,gt=0)

@app.post("/student")
def add_student(student:Student):
    students.append(student)
    return student

@app.get("/Students12")
def Stduent():
    return students