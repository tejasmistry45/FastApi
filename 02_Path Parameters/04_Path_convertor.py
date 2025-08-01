# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:

from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"File Path": file_path}