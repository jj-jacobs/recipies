from config import app
from controler_functions import register, login, home, dash
from models import User, Recipie

app.add_url_rule("/register", view_func = register, methods = ["GET", "POST"])

app.add_url_rule("/login", view_func = login)

app.add_url_rule("/", view_func = home)

app.add_url_rule("/dashboard", view_func = dash, methods = ["GET", "POST"])