#controllers/login/checkLogged.py
import config
from bottle import request

def call():
    userID = request.get_cookie('userID', secret=config.kdict['SECRET_KEY'])
    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

    if(userID and userRole):
        return userID