#controllers/login/checkLogged.py
import config
from bottle import request

def call():
    user = request.get_cookie('userID', secret=config.kdict['SECRET_KEY'])
    return user