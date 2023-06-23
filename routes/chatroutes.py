from flask import Blueprint
from controllers.chatcontroller import allchats, mychats, addchat, mychat, editchat, chatpassword, deletechat, chat

chat_bp = Blueprint('chat', __name__)

chat_bp.add_url_rule('/allchats', view_func=allchats)
chat_bp.add_url_rule('/mychats', view_func=mychats)
chat_bp.add_url_rule('/addchat', methods=['GET', 'POST'], view_func=addchat)
chat_bp.add_url_rule('/mychat/<id>', methods=['GET', 'POST'], view_func=mychat)
chat_bp.add_url_rule('/editchat/<id>', methods=['GET', 'POST'], view_func=editchat)
chat_bp.add_url_rule('/chatpassword/<id>', methods=['GET', 'POST'], view_func=chatpassword)
chat_bp.add_url_rule('/deletechat/<id>', methods=['GET', 'POST'], view_func=deletechat)
chat_bp.add_url_rule('/chat/<id>', methods=['GET', 'POST'], view_func=chat)