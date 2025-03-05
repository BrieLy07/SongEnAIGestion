from flask import Flask, request, jsonify
from services.generate_music import generate_music, get_audio
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return jsonify({"message": "Bienvenido a SongGenIA API"})

@app.route("/generate-music", methods=["POST"])
def generate_song():
    data = request.get_json()
    lyrics = data.get("lyrics")
    genre = data.get("genre")
    mood = data.get("mood")

    if not lyrics or not genre or not mood:
        return jsonify({"error": "Faltan parámetros"}), 400

    response = generate_music(lyrics, genre, mood)
    return jsonify(response)

@app.route("/get-audio/<task_id>", methods=["GET"])
def check_audio(task_id):
    response = get_audio(task_id)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
