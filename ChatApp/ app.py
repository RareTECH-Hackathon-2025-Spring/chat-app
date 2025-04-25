from flask import Flask
from Blueprint.auth import auth_bp
from Blueprint.channels import channels_bp
from Blueprint.messages import messages_bp
from Blueprint.worktime import worktime_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(channels_bp)
app.register_blueprint(messages_bp)
app.register_blueprint(worktime_bp)

if __name__ == "__main__":
    app.run(debug=True)