#HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1. Let's make a FastAPI app (that means API) first

app = FastAPI(title="Calculator API")
@app.post("/multiply")
def multiply(a: float, b: float):
    """Multiplies two numbers.

    args: a (float): The first number.
            b (float): The second number.
    
    returns: float: The product of the two numbers.
    """
    result = a * b
    return {"result": result}

@app.post("/add")
def add_numbers(x: float, y: float):
    """Adds two numbers.

    args: x (float): The first number.
            y (float): The second number.
    
    returns: float: The sum of the two numbers.
    """
    result = x + y
    return {"result": result}

@app.post("/subtract")
def subtract(a: float, b: float):
    """Subtracts the second number from the first number.

    args: a (float): The first number.
            b (float): The second number.
    
    returns: float: The difference of the two numbers.
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
def divide(a: float, b: float):
    """Divides the first number by the second number.

    args: a (float): The numerator.
            b (float): The denominator.
    returns: float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    result = a / b
    return {"result": result}



#2 . Convert FastAPI app to FastMCP app
mcp = FastApiMCP(app,name="CalculatorMCP")
mcp.mount_http()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)