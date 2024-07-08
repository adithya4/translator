from fastapi import FastAPI
import googletrans import Translator

app= FastAPI()

translator = Translator()

@app.get("/transalte")
def index():
  user_text = "apa kabar"
  languages = "en"
  translated_text = translator.translate(user_text, dest="languages")
  return translated_text
  

