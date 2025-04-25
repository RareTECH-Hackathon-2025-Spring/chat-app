from flask import Blueprint, session, redirect, url_for, render_template

channels_bp = Blueprint('channels', __name__, url_prefix='/channels')

#@app.route ではなく、 @channels_bp.route を使用