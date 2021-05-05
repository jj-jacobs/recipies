from flask import Flask, render_template, request, redirect, flash, session
from config import db
from models import User, Recipie

def register():
    validation_check = User.validate_user(request.form)
    print("this is the requeset from the form")
    print(request.form)
    if not validation_check:
        return render_template('home.html')
    else:
        new_user = User.add_new_user(request.form)
        session["user_id"] = new_user.id
        return redirect('/dashboard')

def login():
    return render_template('login.html')

def home():
    return render_template('home.html')

def dash():
    return render_template('dashboard.html')
