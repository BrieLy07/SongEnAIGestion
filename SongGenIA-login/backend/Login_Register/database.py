import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()


db = SQLAlchemy()

def init_db(app):
    """Inicializa la conexión a la base de datos"""
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?connect_timeout=60&read_timeout=60"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        try:
            db.engine.connect()
            print('Conectado a MySQL con SQLAlchemy')
            # Crear tablas solo si no existen
            db.create_all()
        except Exception as e:
            print(f'Error al conectar con MySQL: {e}')