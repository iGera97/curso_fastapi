from fastapi import FastAPI
from Routes.main_route import router
app = FastAPI()

app.include_router(router)