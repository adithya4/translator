from fastapi import FastAPI
from googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/translate")
def index():
  user_text = "apa kabar"
  languages = "en"
  translated_text = translator.translate(user_text, dest="languages")
  return translated_text.text
  

