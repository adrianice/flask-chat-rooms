from flask import render_template, request, redirect, flash, session
from flask_login import current_user
from models.ModelChat import ModelChat
from models.entities.Chat import Chat
from db import mysql

def allchats():
    if current_user.is_authenticated:
        return render_template('allchats.html', chats = ModelChat.getAllChats(mysql))
    return redirect('/login')

def mychats():
    if current_user.is_authenticated:
        return render_template('mychats.html', chats = ModelChat.getMyChats(mysql, current_user.get_id()))
    return redirect('/login')

def addchat():
    if current_user.is_authenticated:
        if request.method == 'POST':
            chat = Chat(0, current_user.get_id(), request.form['password'], request.form['name'], request.form['description'])
            ModelChat.insertChat(mysql, chat)
            flash("Chat created succesfully.", "success")
            return redirect('/mychats')
        return redirect('/allchats')
    return redirect('/')

def mychat(id):
    if current_user.is_authenticated:
        mychats = ModelChat.getMyChatsId(mysql, current_user.get_id())
        if (int(id),) in list(mychats):
            return render_template('mychat.html', chat = ModelChat.getChat(mysql, id))
        return redirect('/mychats')
    return redirect('/')

def editchat(id):
    if current_user.is_authenticated:
        mychats = ModelChat.getMyChatsId(mysql, current_user.get_id())
        if (int(id),) in list(mychats):
            ModelChat.updateChat(mysql, id, request.form['name'], request.form['description'])
            flash("Chat updated successfully.", "success")
            return redirect(f'/mychat/{id}')
        return redirect('/mychats')
    return redirect('/')

def chatpassword(id):
    if current_user.is_authenticated:
        mychats = ModelChat.getMyChatsId(mysql, current_user.get_id())
        if (int(id),) in list(mychats):
            ModelChat.updateChatPassword(mysql, id, request.form['password'])
            flash("Password updated successfully.", "success")
            return redirect(f'/mychat/{id}')
        return redirect('/mychats')
    return redirect('/')

def deletechat(id):
    if current_user.is_authenticated:
        mychats = ModelChat.getMyChatsId(mysql, current_user.get_id())
        if (int(id),) in list(mychats):
            ModelChat.deleteChat(mysql, id)
            flash("Chat deleted succesfully.", "success")
        return redirect('/mychats')
    return redirect('/')

def chat(id):
    if current_user.is_authenticated:
        session['chat_id'] = id
        chat = ModelChat.getChat(mysql, id)
        if request.method == 'POST':
            if chat[2] == request.form['password']:
                return render_template('chat.html', chat = ModelChat.getChat(mysql, id), user_id = current_user.get_id())
            flash("Incorrect password.", "warning")
            return render_template('chatpassword.html')
        if chat[2] == "":
            return render_template('chat.html', chat = ModelChat.getChat(mysql, id), user_id = current_user.get_id())
        return render_template('chatpassword.html')
    return redirect('/')
