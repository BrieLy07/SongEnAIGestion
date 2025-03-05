import requests
from config import API_KEY

API_URL = "https://apibox.erweima.ai/api/v1/generate"

# 📌 URL de callback (puede ser un webhook público o tu propio backend)
CALLBACK_URL = "https://webhook.site/tu-url-de-prueba"  # Cambia esto

def get_audio(task_id):
    """Consulta el estado de la generación de audio y extrae los enlaces."""
    url = f"https://apibox.erweima.ai/api/v1/generate/record-info?taskId={task_id}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        print("Estado de la tarea:", response.status_code, response.text)

        if response.status_code == 200:
            data = response.json()
            suno_data = data.get("data", {}).get("response", {}).get("sunoData", [])
            
            # Extraer los enlaces de los audios generados
            audio_links = []
            for song in suno_data:
                audio_links.append({
                    "streamAudioUrl": song.get("streamAudioUrl"),
                    "sourceStreamAudioUrl": song.get("sourceStreamAudioUrl")
                })

            return {"taskId": task_id, "audio_links": audio_links}
        else:
            return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}




def generate_music(lyrics, genre, mood, custom_mode=True, instrumental=False):
    """Genera música con la API de Suno AI."""
    if not API_KEY:
        return {"error": "No se encontró la clave API."}

    # 📌 Si customMode es True, necesitamos más datos
    if custom_mode:
        payload = {
            "customMode": True,
            "estilo": genre,
            "titulo": "Canción generada",
            "mensaje": lyrics,
            "instrumental": instrumental,
            "callBackUrl": CALLBACK_URL  # 📌 Agregamos la URL de callback
        }
    else:
        # 📌 Si customMode es False, solo enviamos mensaje y callback
        payload = {
            "customMode": False,
            "mensaje": lyrics,
            "callBackUrl": CALLBACK_URL  # 📌 Agregamos la URL de callback
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        
        # 📌 Ver respuesta completa en la consola
        print("Respuesta de Suno AI:", response.status_code, response.text)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as e:
        return {"error": str(e)}
    

    