# Create an Enum class
# https://fastapi.tiangolo.com/tutorial/path-params/#create-an-enum-class

from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, 
                "message": "Deep Learning FWT!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, 
                "message": "LeCNN all the Images"}
                
    if model_name is ModelName.resnet:
        return {"Model Name": model_name,
                "Message": f"This is New Model called {model_name}"}
    
    return {"model_name": model_name, 
            "message": "Have some residuals"}
