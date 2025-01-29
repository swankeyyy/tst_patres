from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from app.api import router


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

app.include_router(router)

@app.get("/")
def main():
    return RedirectResponse(url='/docs')
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
