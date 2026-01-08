from fastapi import FastAPI
from .database import Base, engine
from .api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Profile Management API")
app.include_router(router)
