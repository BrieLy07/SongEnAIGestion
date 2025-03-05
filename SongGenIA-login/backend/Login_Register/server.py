import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from Login_Register.__init__ import create_app
from flask_cors import CORS

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))  # Puedes cambiar el valor predeterminado del puerto aquí si lo necesitas
    app.run(host='0.0.0.0', port=port, debug=True)  # Debug debe ser False en producción
