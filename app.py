from fastapi import FastAPI 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

data = []

class Person(BaseModel):
    name: str
    occuption: str
    address: str

@app.get("/person")
async def get_all_persons():
    return data

@app.post("/person")
async def create_new_person(person_request: Person):
    if not person_request.name or not person_request.address or not person_request.occuption:
       false = False
       details = {"success": false,
                  "result": {"error message":"invalid request"} }
       person_request = details
    
    else: 
        true = True
        data.append(person_request)
        details = {"success": true,
                  "result": person_request }
        person_request = details

    person_json = jsonable_encoder(person_request)

    return person_json