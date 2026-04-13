# from fastapi import FastAPI,Depends,Header,HTTPException
# app=FastAPI()


# def mydependency():
#     return "Hello"
# @app.get("/")
# def home(data:str=Depends(mydependency)):
#     return {"msg":data}


# def from fastapi import Header

# from fastapi import FastAPI, Depends, Header, HTTPException

# app = FastAPI()

# def verify_token(token: str = Header(...)):
#     print("🔥 HEADER RECEIVED:", token)

#     if token != "token123":
#         raise HTTPException(status_code=401, detail="Unauthorized")

#     return token

# def get_current_user(token: str = Depends(verify_token)):
#     return {"User name": "Jairam"}

# @app.get("/profile")
# def profile(user=Depends(get_current_user)):
#     return user

# app=FastAPI()


# def verify_user(token:str=Header(...)):
#     if token!="Token123":
#         raise HTTPException(status_code=401,detail="Unauthorized")
#     return token
    
# def get_cuurent_user(token:str=Depends(verify_user))
#     return {"user":"Jairam"}
# @app.get('/profile')
# def profile(user=Depends(get_cuurent_user)):
#     return {
#         "message":"Verified",
#         "user":"user"
#     }


# def deep_common():
#     print("running dependency")
#     return "data"

# @app.get("/test")
# def test(
#     a=Depends(deep_common,use_cache=False),
#     b=Depends(deep_common,use_cache=False)
# ):
#     return {"a":a,"b":b}

# from fastapi import FastAPI,Request

# app=FastAPI()

# @app.middleware("http")
# async def log_requests(request:Request,call_next):
#     print("Request recieved:",request.url)

#     response= await call_next(request)

#     print("response sent")

#     return response
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# @app.middleware("http")
# async def auth_middleware(request: Request, call_next):

#     # Allow docs
#     if request.url.path in ["/docs", "/openapi.json", "/docs/oauth2-redirect"]:
#         return await call_next(request)

#     auth = request.headers.get("Authorization")

#     if auth != "Bearer token123":
#         return JSONResponse(
#             status_code=401,
#             content={"detail": "Unauthorized"}
#         )

#     response = await call_next(request)
#     return response

# @app.get("/profile")
# def profile():
#     return {"user": "Jairam"}

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Fake login
@app.post("/login")
def login():
    data = {"sub": "jairam"}  # user info
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

# Protected route
@app.get("/profile")
def profile(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"user": payload["sub"]}
    except:
        raise HTTPException(status_code=401, detail="Invalid token") 