
from fastapi import FastAPI
from pydantic import BaseModel


# Use flake8 to enforce clean code and readable code.
app = FastAPI()

# class name starts with uppercase eg. Number or MathOperationRequest.
class number(BaseModel):
    value: float

@app.post("/multiply/")
async def multiply_number(number: number):
    multiply=number.value*number.value
    # return is a string

    return("multiply=",multiply)

    # return {"multiply": multiply}
    # return


@app.post("/division/")
async def division_number(request, request_body: Number):
    division=number.value/2
    return ("division=",division)

@app.post("/sum/")
async def sum_number(number: number):
    sum = number.value + number.value
    return ("sum=",sum)


# @app.post("/division/")
# async def division_number(request, request_body: MathOperationRequest):
#     division=request_body.value/2
#     return {"division": division}

"""
write unit tests with pytest to test your application
modify your application so it runs in a docker container.
it should be able to install all dependencies,run in docker, expose a port so you can communicate with the app 
"""
