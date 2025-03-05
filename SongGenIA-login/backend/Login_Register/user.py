from Login_Register.database import db
from flask_login import UserMixin
from passlib.hash import bcrypt

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convierte el objeto User a un diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cedula': self.cedula,
            'telefono': self.telefono,
            'email': self.email,
            'username': self.username
        }

    def check_password(self, password):
        """Método para verificar la contraseña (deberías usar bcrypt para encriptar y verificar)"""
        return bcrypt.verify(password, self.password)

    def set_password(self, password):
        """Método para encriptar la contraseña"""
        self.password = bcrypt.hash(password)