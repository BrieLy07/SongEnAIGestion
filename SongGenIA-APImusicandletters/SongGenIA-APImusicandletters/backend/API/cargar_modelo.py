import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Obtener la ruta absoluta del directorio actual
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta absoluta del modelo convertido
ruta_modelo_keras = os.path.join(ruta_base, "..", "models", "modelo_nuevo.keras")

# Verificar si el archivo existe antes de cargarlo
if not os.path.exists(ruta_modelo_keras):
    raise FileNotFoundError(f"❌ ERROR: El archivo {ruta_modelo_keras} no existe. Verifica la ruta.")

# Cargar el modelo
modelo = load_model(ruta_modelo_keras)

# Mostrar resumen del modelo
modelo.summary()

print("✅ Modelo cargado exitosamente.")
