import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from ChatApp.Blueprint.auth import auth_bp
from ChatApp.Blueprint.channels import channels_bp
from ChatApp.Blueprint.messages import messages_bp
from ChatApp.Blueprint.worktime import worktime_bp

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your-very-secret-key'

app.register_blueprint(auth_bp)
app.register_blueprint(channels_bp)
app.register_blueprint(messages_bp)
app.register_blueprint(worktime_bp)

@app.route('/')
def home():
    return "http://127.0.0.1:5000/auth/login"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
