from flask import Blueprint, session, redirect, url_for, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#@app.route ではなく、 @auth_bp.route を使用