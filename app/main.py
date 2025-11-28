from fastapi import FastAPI
import uvicorn
import json 


app = FastAPI(
    title="(._.)"
)

@app.get("/")
async def root():
    return {
        "status": 200,
        "message": "hello"
    }

@app.get("/users")
async def get_users():
    with open("app/data.json", "r") as file:
        data = json.load(file)

    return {
        "status": 200,
        "users": data["users"]
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)