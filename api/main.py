from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API"}


handler = Mangum(app=app)
