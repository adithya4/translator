from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/",response_class=HTMLResponse)
def index():
  with open("index.html",'r') as file:
    return file.read()



  

