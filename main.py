from fastapi importFastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def index():
  return "HI"

