from flask import Blueprint, session, redirect, url_for, jsonify, request, current_app
from flask_oauthlib.client import OAuth
from flask_login import login_required, logout_user
from werkzeug.exceptions import HTTPException


auth_bp = Blueprint('auth', __name__, url_prefix='/login/auth')

# Inicialización del objeto OAuth
oauth = OAuth()

def init_oauth_routes(auth_bp):
    
    google = oauth.remote_app(
        'google',
        consumer_key=current_app.config['GOOGLE_CLIENT_ID'],
        consumer_secret=current_app.config['GOOGLE_CLIENT_SECRET'],
        request_token_params={
            'scope': 'email',
            'response_type': 'code',
        },
        base_url='https://www.googleapis.com/oauth2/v1/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
    )

    @auth_bp.route('/google')
    def google_login():
        return google.authorize(callback=url_for('auth.google_auth_callback', _external=True))

    @auth_bp.route('/google/callback')
    def google_auth_callback():
        response = google.authorized_response()
        if response is None or response.get('access_token') is None:
            return 'Access denied: reason={} error={}'.format(
                request.args['reason'],
                request.args['error_description']
            )

        session['google_token'] = (response['access_token'], '')
        user_info = google.get('userinfo')
        # Aquí, 'userinfo' es el endpoint de Google para obtener la información del usuario.
        return jsonify(user_info.data)

    @auth_bp.route('/logout')
    @login_required
    def logout():
        logout_user()
        session.clear()
        return redirect('/')
