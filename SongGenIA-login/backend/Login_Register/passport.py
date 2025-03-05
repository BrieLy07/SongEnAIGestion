import os
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from Login_Register.user import User

login_manager = LoginManager()
oauth = OAuth()

def init_passport(app):
    """Inicializa la autenticación con Google y configura flask-login"""
    
    # Inicializa el LoginManager y OAuth con la app Flask
    login_manager.init_app(app)
    oauth.init_app(app)
    
    # Configuración para Google OAuth
    google = oauth.register(
        name='google',
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params={'scope': 'openid email profile'},
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
        client_kwargs={'scope': 'openid email profile'},  # Asegurarse de incluir el perfil completo
        jwks_uri="https://www.googleapis.com/oauth2/v3/certs",  # Esto evita el error de 'jwks_uri'
    )

    # Configura el cargador de usuarios para Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        """Carga un usuario desde la base de datos usando su ID"""
        return User.query.get(int(user_id))
    
    return google
