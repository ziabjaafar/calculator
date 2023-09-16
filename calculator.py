
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class number(BaseModel):
    value: float

@app.post("/multiply/")
async def multiply_number(number: number):
    multiply=number.value*number.value
    return("multiply=",multiply)


@app.post("/division/")
async def division_number(number: number):
    division=number.value/2
    return ("division=",division)

@app.post("/sum/")
async def sum_number(number: number):
    sum = number.value + number.value
    return ("sum=",sum)
