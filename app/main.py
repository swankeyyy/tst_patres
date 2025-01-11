from fastapi import FastAPI

import uvicorn


app = FastAPI(
    title="Library",
    description="test task for Patres",
    version="0.0.1",
    contact={
        "name": "Ivan Levchuk",
        "email": "swankyyy1@gmail.com",
    },
)


@app.get("/")
async def index():
    return "Hello world"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
