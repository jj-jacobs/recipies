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
    
    return redirect('/dashboard')

def home():
    return render_template('home.html')

def dash(): 
    user_i_need = User.query.get(session["user_id"])
    fname  = user_i_need.first_name
    return render_template('dashboard.html', first_name = fname)

def create():
    return render_template('create.html')

def make_recipie():    
    new_recipie= Recipie.add_new_recipie(request.form)
    return redirect('/review')

def review():
    recipie_review = Recipie.query.get(session["user_id"])
    recipies  = recipie_review
    return render_template('review.html', recipies = recipies)