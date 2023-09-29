from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MathOperationrequest(BaseModel) :
    value:float

@app.post("/multiply/")
async def multiply_number(multiply: MathOperationrequest):
    multiply=multiply.value*multiply.value
    return {"multiply": multiply}

@app.post("/division/")
async def division_number(division: MathOperationrequest):
    division=division.value/2
    return {"division": division}


@app.post("/sum/")
async def sum_number(sum: MathOperationrequest):
    sum=sum.value+sum.value
    return {"sum": sum}