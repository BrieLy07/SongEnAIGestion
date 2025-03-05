from flask import Flask, request, jsonify
from preprocesar_texto import generar_texto  # Importamos la función ya existente

app = Flask(__name__)

@app.route('/generar', methods=['POST'])
def generar():
    """Recibe una frase inicial y genera texto basado en el modelo"""
    data = request.get_json()
    
    if "frase_inicial" not in data:
        return jsonify({"error": "Debe incluir 'frase_inicial' en la solicitud"}), 400
    
    frase_inicial = data["frase_inicial"]
    texto_generado = generar_texto(frase_inicial)  # Llama a la función de preprocesar_texto.py
    
    return jsonify({
        "frase_inicial": frase_inicial,
        "texto_generado": texto_generado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
