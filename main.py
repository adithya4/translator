from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/",response_class=HTMLResponse)
def index():
  with open("index.html",'r') as file:
    return file.read()

@app.get("/translate")
def translation(user_text : str=Form(...), language: str=Form(...)):
  translated_text = translator.translate(user_text, dest=language)
  return translated_text.text
  

  

