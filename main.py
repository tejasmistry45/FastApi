from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    with open('./patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hellow():
    return {'message': "Patient Management System"}

@app.get("/about")
def about():
    return {"message" : "THis is About Page and you are welcome here!"}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description="ID of Patient is Required", example="P001")):

    # load all the patients data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {"error: Patient Not Found"}
    
