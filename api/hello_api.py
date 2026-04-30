"""Hello World FastAPI examples — path params, query params, defaults."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    """No parameters, just a simple greeting."""
    return "Hello, world!"


# http://127.0.0.1:8000/


@app.get("/greet/{name}")
def greet(name: str):
    """Name is a string, and it is required."""
    return f"Hello, {name}!"


# http://127.0.0.1:8000/greet/Daria


@app.get("/greet_with_name")
def greet_with_name(name: str = "Daria"):  # ← default value
    """Name is a string, and it has a default value of 'Daria'."""
    return f"Hello, {name}!"


# http://127.0.0.1:8000/greet_with_name?name=Alice


@app.get("/greet_int")
def greet_int(num: int = 42):  # ← default value
    """Num is an integer, and it has a default value of 42."""
    return f"Hello, number {num}!"


# http://127.0.0.1:8000/greet_int?num=100


@app.get("/greet_2/{name}")
def greet_2(name: str, age: int | None = None):
    """Age is optional, it can be None."""
    if age is not None:
        return f"Hello, {name}, age {age}!"
    return f"Hello, {name}!"


# http://127.0.0.1:8000/greet_2/Daria?age=28
