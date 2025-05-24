from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Numb(BaseModel):
    a: float
    b: float

class BasicMath(Numb):
    function: str

@app.post("/add(+)")
def add_math(n: Numb):
    math_result = n.a + n.b
    return {"function": "add(+)", "a":n.a, "b": n.b, "math_result": math_result}

@app.post("/substract(-)")
def substract_math(n: Numb):
    math_result = n.a - n.b
    return {"function": "substract(-)", "a": n.a, "b": n.b, "math_result": math_result}

@app.post("/multiply(*)")
def multiply_math(n: Numb):
    math_result = n.a * n.b
    return {"function": "multiply(*)", "a": n.a, "b": n.b, "math_result": math_result}

@app.post("/divide(/)")
def divide_math(n: Numb):
    math_result = n.a / n.b
    return {"function": "divide(/)", "a": n.a, "b": n.b, "result": math_result}
