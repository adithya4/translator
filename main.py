from fastapi importFastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def index():
  return "HI"

if __name__ == "__main__":
  uvicorn.run(app,host="0.0.0.0",port=10000)
