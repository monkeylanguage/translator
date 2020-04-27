import json
from flask import Flask, jsonify, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()
app.config['SECRET_KEY'] = 'elcepelcedopekelce'

@app.route('/', methods=['POST'])
def login():

    data = request.get_data()
    text2translate = "error"
    translation = ":("

    try:
        json_data = json.loads(data)
        api_key = json_data.get("apikey", "")

        if api_key == "<s;_xLFj<ab,O{e":
            text2translate = json_data.get("text", "")
            translation = translator.translate(text2translate, dest='cs').text
        else:
            pass

    except:
        pass

    return jsonify(translation=translation, text=text2translate)
