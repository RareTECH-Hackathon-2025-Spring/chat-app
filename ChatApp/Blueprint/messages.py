from flask import Blueprint, session, redirect, url_for, render_template

messages_bp = Blueprint('messages', __name__, url_prefix='/messages')

#@app.route ではなく、 @messages_bp.route を使用