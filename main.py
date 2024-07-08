from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/transalte")
def index():
  return "HI"

