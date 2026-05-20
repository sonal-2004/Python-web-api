from fastapi import FastAPI

app = FastAPI(
    title="My First API",
    description="Simple FastAPI project with Swagger UI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "API is running"
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello World"
    }

@app.get("/user/{name}")
def get_user(name: str):
    return {
        "user": name
    }