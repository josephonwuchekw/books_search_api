from fastapi import FastAPI
from mangum import Mangum
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
google_api_key = os.getenv("GOOGLE_API_KEY")


@app.get("/")
def root():
    return {"message": google_api_key}


handler = Mangum(app=app)
