from db import socketio, mysql
from flask_socketio import emit, join_room
from flask import session
from flask_login import current_user
from models.entities.Message import Message
from models.ModelMessage import ModelMessage
from datetime import date, datetime

@socketio.on('connect')
def onConnect():
    chat_id = session['chat_id']
    join_room(chat_id)

    socketio.emit('receive-all-messages', ModelMessage.getAllMessages(mysql, chat_id), room = session['chat_id'])

@socketio.on('send-message')
def sendMessage(data):
    message = Message(0, session['chat_id'], current_user.get_id(), data['message'])
    ModelMessage.insertMessage(mysql, message)

    messageInfo = {"id_user":current_user.get_id(), 
                   "username": current_user.username, 
                   "message": data['message'], 
                   "date": str(date.today()), 
                   "time": datetime.now().strftime("%H:%M")}
    
    socketio.emit('recieve_message', messageInfo , room = session['chat_id'])
