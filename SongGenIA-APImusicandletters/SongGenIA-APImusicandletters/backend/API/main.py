from flask import Flask, request, jsonify
from services.generate_music import generate_music, cargar_letra_desde_archivo, get_audio  # Cambié los nombres a los correctos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Bienvenido a SongGenIA API"})

@app.route("/generate-music", methods=["POST"])
def generate_song():
    data = request.get_json()
    genre = data.get("genre", "pop")  # Usamos 'pop' como valor predeterminado para el género

    response = generate_music(genre, "happy")  # Llamamos a la función con el género y el estado de ánimo (ejemplo)

    if "task_id" in response:
        return jsonify({"task_id": response["task_id"]}), 200
    else:
        return jsonify(response), 500

@app.route("/get-audio/<task_id>", methods=["GET"])
def check_audio(task_id):
    response = get_audio(task_id)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
