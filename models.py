from flask import flash, session
from sqlalchemy.sql import func
from config import db, bcrypt, re

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    confirm_pass = db.Column(db.String(255))
    @classmethod
    def validate_user(cls, user_data):
        print(user_data)
        is_valid = True
        if len(user_data["fn"]) < 1:
            is_valid = False
            flash("Please provide a first name")
        if len(user_data["ln"]) < 1:
            is_valid = False
            flash("Please provide a last name")
        # if not EMAIL_REGEX.match(user_data["em"]):
        #     is_valid = False
        #     flash("Please provide a valid email")
        if len(user_data["pw"]) < 8:
            is_valid = False
            flash("Password should be at least 8 characters")
        if user_data["pw"] != user_data["confirm_pass"]:
            is_valid = False
            flash("Passwords do not match")
        return is_valid
    @classmethod
    def add_new_user(cls, user_data):
        hashed_password = bcrypt.generate_password_hash(user_data["pw"])
        user_to_add = cls(first_name=user_data["fn"], last_name=user_data["ln"], email=user_data["em"], password=hashed_password)
        db.session.add(user_to_add)
        db.session.commit()
        return user_to_add
class Recipie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    time = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "cascade"), nullable = False)