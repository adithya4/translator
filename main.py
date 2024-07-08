from fastapi import FastAPI, Form 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from googletrans import Translator

app= FastAPI()

translator = Translator()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/",response_class=HTMLResponse)
def index():
  with open("index.html",'r') as file:
    return file.read()

@app.post("/translate")
async def translation(user_text : str=Form(...), language: str=Form(...)):
  translated_text = translator.translate(user_text, dest=language)
  return {"translated_text" : translated_text.text}
  

  

