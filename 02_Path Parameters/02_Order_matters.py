from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"message": "The Current User"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}