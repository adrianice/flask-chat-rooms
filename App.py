from routes.loginroutes import login_bp
from routes.chatroutes import chat_bp
from chatSocket import onConnect
from db import app

#Import routes
app.register_blueprint(login_bp)
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    
    app.run(port=5000, host='0.0.0.0')