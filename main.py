from fastapi import FastAPI
from endpoints import router

app = FastAPI()

app.include_router(router=router, prefix="/v1")
