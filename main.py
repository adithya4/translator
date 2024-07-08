from fastapi import FastAPI
from googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/")
def home():
  return "WELCOME HOME"

@app.get("/translate")
def index(user_text : str=Form(...), languages: str=Form(...)):
  translated_text = translator.translate(user_text, dest=languages)
  return translated_text.text
  

