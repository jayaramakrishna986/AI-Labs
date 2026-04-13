from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from fastapi import HTTPException,Header,Query
from typing import Optional,List,Dict
app=FastAPI()

# class employee(BaseModel):
#     id:int
#     name : str = Field(...,min_length=3,max_length=9)
#     age:int=Field(...,gt=0,lt=100)

# Employees=[]

# @app.get("/Employee")
# def Employee():
#     return Employees

# @app.post("/Employee/add/")
# async def add_employee(employee:employee):
#     Employees.append(employee)
#     # raise  HTTPException(statuscode=404,detail="print emplyee is uable to add")

# @app.delete("/Employee/delete/{emp_id}")
# def deleteemployee(emp_id:int):
#     for i in Employees:
#         if i.id==emp_id:
#             Employees.remove(i)
        
#     raise HTTPException(status_code=404,detail="Employee is not found")
from pydantic import field_validator

# class Student(BaseModel):
#     id :int =Field(...,gt=0,lt=100)
#     name:str=Field(...,min_length=3,max_length=100)
#     des:Optional[str]=None
#     status:str="pending"
#     subjects:List[str]
#     Marks:Dict[str,str]
#     class debug():
#         orm_ode=True


# class People(BaseModel):
#     name :str
#     age:str
#     @field_validator
#     def name_is_valid(cls,value):
#         if any(value.isdigit() for char in value):
#             raise ValueError("Name should not contain numbers")
#         return value
    

# class stduent(BaseModel):
#     name:str=Field(...,min_length=3)
#     age:int=Field(...,gt=0)
#     des:Optional[str]=None
#     list1=list[str]
#     dict1=Dict[str,str]

#     @field_validator("name")
#     def namisvlaid(cls,value):
#         if any(value.isdigit() for char in value):
#             raise ValueError("E")
        


# @app.get("/users")
@app.get("/users")
def usersnames(user_agent: str = Query(...)): # Must be Query(...)
    return {"User_agent": user_agent}


def user(useragent:str=Query(...)):
    # <form>

    # <input name="username">
    # <input pass1-="password">
    # </form>