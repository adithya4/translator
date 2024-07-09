
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route("/", methods=["GET"])
def index():
    with open("index.html", 'r') as file:
        return render_template_string(file.read())

@app.route("/translate", methods=["POST"])
def translation():
    user_text = request.form['user_text']
    language = request.form['language']
    translated_text = translator.translate(user_text, dest=language)
    return jsonify({"translated_text": translated_text.text})

