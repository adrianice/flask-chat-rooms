from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
from flask_session import Session
from flask_login import LoginManager
from config import config
from models.ModelUser import ModelUser


app = Flask(__name__)
app.config.from_object(config['development'])

mysql = MySQL(app)
socketio = SocketIO(app)
Session(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)

def status_404(error):
    return render_template('404.html')

app.register_error_handler(404, status_404)