
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from api.ai_endpoints import ai_router

app = FastAPI()
app.include_router(ai_router)
