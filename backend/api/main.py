from fastapi import FastAPI

from api.routers.users import router as user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def root():
    return {"Hello": "World :^)"}
