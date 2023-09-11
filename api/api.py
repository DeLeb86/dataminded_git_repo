from fastapi import FastAPI
api=FastAPI()

@api.get("/hello")
def print_hello():
    print("Hello there")