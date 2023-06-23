from flask import render_template, request, redirect, flash
from flask_login import login_user, logout_user, current_user
from models.ModelUser import ModelUser
from models.entities.User import User
from db import mysql, login_manager_app

def index():
    if current_user.is_authenticated:
        return redirect('/allchats')
    return redirect('/login')

def login():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(mysql, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect('/')
            else:
                flash("Username or password incorrect.", "warning")
        else:
            flash("Username or password incorrect.", "warning")
    return render_template('login.html')

def signin():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        exist_user = ModelUser.insertUser(mysql, user)
        if(exist_user != None): 
            flash("User correctly registered.", "success")
            return redirect('/login')
        else:
            flash("User already exists.", "danger")
    return render_template('signin.html')

def logout():
    logout_user()
    return redirect('/login')
