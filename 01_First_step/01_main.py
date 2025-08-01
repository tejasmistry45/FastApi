# https://fastapi.tiangolo.com/tutorial/first-steps/#operation

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}