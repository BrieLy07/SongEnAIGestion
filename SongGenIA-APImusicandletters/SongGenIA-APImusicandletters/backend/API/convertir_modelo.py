import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Obtener la ruta absoluta del directorio actual
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta absoluta del modelo .h5
ruta_modelo_h5 = os.path.join(ruta_base, "../models/song_lyrics_generator.h5")

# Cargar el modelo en modo compatibilidad
modelo = load_model(ruta_modelo_h5, compile=False)

# Ruta donde guardaremos el modelo convertido en formato .keras
ruta_modelo_keras = os.path.join(ruta_base, "../models/modelo_nuevo.keras")

# Guardar el modelo en el nuevo formato .keras
modelo.save(ruta_modelo_keras)

print(f"✅ Modelo convertido exitosamente y guardado en: {ruta_modelo_keras}")
