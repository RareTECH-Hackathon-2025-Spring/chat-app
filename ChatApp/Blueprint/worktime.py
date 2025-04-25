from flask import Blueprint, session, redirect, url_for, render_template

worktime_bp = Blueprint('worktime', __name__, url_prefix='/worktime')

#@app.route ではなく、 @worktime_bp.route を使用