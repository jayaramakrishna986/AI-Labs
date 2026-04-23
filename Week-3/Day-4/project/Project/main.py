import time 
from fastapi import FastAPI
import asyncio
app=FastAPI()


@app.get("/1")
async def endpoint1():#processed sequntial
    print("Hello1")
    time.sleep(5)#Blocking I/O operation,cant be awaited
    #Function execution cannot be paused
    print("Bye1")

@app.get("/2")
async def endpoint2():#processed concurrently
    print("Hello2")
    await asyncio.sleep(5)#Non Blocking I/O operations,awaited,
    #Function Execution paused
    print("Bye2")

@app.get("/3")
def endpoint2():#processed paralley
    print("Hello2")
    time.sleep(5)
    print("Bye2")

#Uvicorn > Main Thread
#coroutines

# Use async def for endpoint with non-blocking I/O operations
# Dont use async def for endpoint with block
#Use normal function for endpoints with blocking I/O operations