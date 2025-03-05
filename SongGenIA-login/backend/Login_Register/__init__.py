from flask import Flask, jsonify, url_for
import os
from Login_Register.database import init_db
from Login_Register.passport import init_passport
from Login_Register.auth_controller import register, login, google_callback
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    

    # Cargar variables de entorno
    if not os.getenv('SECRET_KEY') or not os.getenv('GOOGLE_CLIENT_ID') or not os.getenv('GOOGLE_CLIENT_SECRET'):
        raise ValueError("Las variables de entorno SECRET_KEY, GOOGLE_CLIENT_ID o GOOGLE_CLIENT_SECRET no están definidas.")

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
    app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')

    # Inicializar base de datos y autenticación
    init_db(app)
    google = init_passport(app)

    # Rutas de autenticación
    @app.route('/register', methods=['POST'])
    def user_register():
        try:
            return register()
        except Exception as e:
            return jsonify({"msg": "Error al registrar el usuario", "error": str(e)}), 500

    @app.route('/login', methods=['POST'])
    def user_login():
        try:
            return login()
        except Exception as e:
            return jsonify({"msg": "Error al iniciar sesión", "error": str(e)}), 500

    @app.route('/login/auth/google')
    def google_login():
        return google.authorize_redirect(url_for('google_callback_route', _external=True))

    @app.route('/login/auth/google/callback')
    def google_callback_route():
        try:
            return google_callback(google)
        except Exception as e:
            return jsonify({"msg": "Error en la autenticación de Google", "error": str(e)}), 500

    return app
