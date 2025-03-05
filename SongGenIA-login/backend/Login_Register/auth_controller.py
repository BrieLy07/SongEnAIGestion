import os
import jwt
from flask import jsonify, request, session, redirect, url_for
from Login_Register.user import User
from Login_Register.database import db
from flask_login import login_user
from passlib.hash import bcrypt


def register():
    """Registra un nuevo usuario"""
    data = request.json
    nombre = data.get('nombre')
    cedula = data.get('cedula')
    telefono = data.get('telefono')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    
    # Verificar que todos los campos estén presentes
    if not all([nombre, cedula, telefono, email, password, username]):
        return jsonify({"msg": "Todos los campos son obligatorios"}), 400
    
    # Verificar si el usuario ya existe
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "El correo electrónico ya está registrado"}), 400
    
    # Encriptar contraseña
    hashed_password = bcrypt.hash(password)
    
    try:
        # Crear nuevo usuario
        new_user = User(
            nombre=nombre,
            cedula=cedula,
            telefono=telefono,
            email=email,
            password=hashed_password,
            username=username
        )
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"msg": "Usuario registrado correctamente"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Error al registrar el usuario", "error": str(e)}), 500

def login():
    """Inicia sesión de un usuario"""
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Buscar usuario por email
    user = User.query.filter_by(email=email).first()
    
    # Verificar si existe el usuario y la contraseña es correcta
    if not user or not user.check_password(password):
        return jsonify({"msg": "Credenciales inválidas"}), 401
    
    # Generar token JWT
    token = jwt.encode(
        {"id": user.id, "email": user.email},
        os.getenv('SECRET_KEY'),
        algorithm="HS256"
    )
    
   
    login_user(user)
    
    return jsonify({"token": token, "user": user.to_dict()})

def google_callback(google):
    try:
        token = google.authorize_access_token()
        resp = google.get('https://www.googleapis.com/oauth2/v2/userinfo')
        user_info = resp.json()

        user = User.query.filter_by(email=user_info['email']).first()
        if not user:
            user = User(
                nombre=user_info['name'],
                cedula=None,
                telefono=None,
                email=user_info['email'],
                password=None,
                username=user_info['name']
            )
            db.session.add(user)
            db.session.commit()

        login_user(user)
        session['user_id'] = user.id
        
        # Redirigir al frontend con el token
        token = jwt.encode(
            {"id": user.id, "email": user.email},
            os.getenv('SECRET_KEY'),
            algorithm="HS256"
        )
        
        # Redirigir a la página principal del frontend con el token
        return redirect(f'http://localhost:8080/dashboard?token={token}') 
    except Exception as e:
        return jsonify({"msg": "Error al autenticar con Google", "error": str(e)}), 500