import os
import json
import random
import numpy as np
import spacy
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.models import load_model


# ✅ 1. Obtener la ruta base
ruta_base = os.path.dirname(os.path.abspath(__file__))

# ✅ 2. Definir las rutas de los archivos
ruta_modelo = os.path.join(ruta_base, "..", "models", "modelo_nuevo.keras")
ruta_tokenizador = os.path.join(ruta_base, "..", "models", "tokenizer.json")

# ✅ 3. Cargar el modelo
modelo = load_model(ruta_modelo)

# ✅ 4. Cargar el tokenizador desde JSON
if os.path.exists(ruta_tokenizador):
    with open(ruta_tokenizador, "r", encoding="utf-8") as f:
        token_json = f.read()  # Leer el archivo JSON como texto
    
    tokenizador = tokenizer_from_json(token_json)  # ✅ Cargar directamente el tokenizador
    print("✅ Tokenizador cargado correctamente.")
else:
    print("❌ ERROR: No se encontró 'tokenizer.json' en 'models/'. Verifica que lo hayas copiado correctamente.")
    exit()


nlp = spacy.load("es_core_news_sm")
# ✅ 5. Función para preprocesar la entrada del usuario
def preprocesar_texto(texto, max_length=15):
    """Preprocesa el texto eliminando ruido y convirtiéndolo en tokens numéricos."""
    # Normalización del texto
    texto = texto.lower().strip()
    
    # Tokenización usando spaCy
    doc = nlp(texto)
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]  # Lematización y limpieza
    
    if not tokens:  # Evitar secuencias vacías
        return np.zeros((1, max_length))  # Devolver una secuencia de ceros
    
    # Convertir tokens en secuencia numérica
    secuencia = tokenizador.texts_to_sequences([" ".join(tokens)])
    
    # Rellenar o truncar la secuencia
    secuencia_padded = pad_sequences(secuencia, maxlen=max_length, padding="post")

    return secuencia_padded


# ✅ Cargar modelo de lematización en español

def lematizar_texto(texto):
    """Reduce el texto a su forma base para mejorar la interpretación del modelo."""
    doc = nlp(texto)
    return " ".join([token.lemma_ for token in doc])

def nucleus_sampling(predictions, top_p=0.9):
    """Selecciona una palabra usando Top-p (Nucleus Sampling)."""
    sorted_indices = np.argsort(predictions)[::-1]  # Ordenar palabras de mayor a menor probabilidad
    sorted_probs = np.sort(predictions)[::-1]  # Ordenar probabilidades

    cumulative_probs = np.cumsum(sorted_probs)  # Calcular la suma acumulada de probabilidades
    top_p_index = np.where(cumulative_probs > top_p)[0][0]  # Obtener el punto de corte

    selected_indices = sorted_indices[:top_p_index + 1]  # Mantener solo las palabras dentro de Top-p
    if len(selected_indices.shape) > 1:  # Asegurar que sea unidimensional
        selected_indices = selected_indices.flatten()

    if len(selected_indices) == 0:
        return np.argmax(predictions)  # Si no hay selección válida, usar la palabra más probable

    selected_index = np.random.choice(selected_indices)  # Elegir aleatoriamente una dentro del grupo

    return int(selected_index)

def generar_texto(texto_inicial, max_words=20, temperatura=0.5, top_p=0.9):
    """Genera una secuencia de texto con mejor coherencia y sin palabras sin sentido."""
    texto_generado = texto_inicial.lower().split()  # Convertir la entrada en tokens
    ultimas_palabras = set()  # Control de palabras repetidas
    
    for _ in range(max_words):
        entrada_procesada = preprocesar_texto(" ".join(texto_generado))  # Preprocesar

        # Obtener la predicción del modelo
        predicciones = modelo.predict(entrada_procesada)[0]

        # Aplicar temperatura para controlar la diversidad
        predicciones = np.log(predicciones + 1e-8) / temperatura
        exp_preds = np.exp(predicciones)
        predicciones = exp_preds / np.sum(exp_preds)

        # Seleccionar palabras dentro del top-p
        indice_palabra = nucleus_sampling(predicciones, top_p)
        palabra_generada = tokenizador.index_word.get(indice_palabra, None)

        # Evitar repeticiones y asegurar contexto
        if not palabra_generada or palabra_generada in ultimas_palabras:
            continue

        ultimas_palabras.add(palabra_generada)
        if len(ultimas_palabras) > 4:
            ultimas_palabras.pop()  # Mantener las últimas 4 palabras en la memoria

        # Detener si se genera un signo de puntuación o palabra sin sentido
        if palabra_generada in [".", ",", "!", "?"]:
            break  

        texto_generado.append(palabra_generada)

    # Verificar si el texto generado es suficiente
    if len(texto_generado) == 0:
        print("❌ ERROR: No se pudo generar texto válido.")
        return ""

    # Guardar la letra generada en un archivo
    with open("letra_generada.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(texto_generado))

    return " ".join(texto_generado)

# ✅ 7. Prueba del sistema
if __name__ == "__main__":
    entrada_usuario = input("🎶 Escribe una palabra o frase inicial: ")
    resultado = generar_texto(entrada_usuario)  # ✅ USAR LA FUNCIÓN CORRECTA
    print(f"🎤 Texto generado: {resultado}")
