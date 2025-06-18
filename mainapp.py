from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello! Use /hello?name=YourName to get a greeting."}

@app.get("/hello")
def say_hello(name: Optional[str] = "friend"):
    return {"message": f"Nice to meet you, {name}!"}
