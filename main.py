from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/",response_class=HTMLResponse)
def home():
  with open("index.html",'r') as file:
    return file.read()


@app.get("/translate")
def index(user_text : str=Form(...), languages: str=Form(...)):
  translated_text = translator.translate(user_text, dest=languages)
  return translated_text.text
  

