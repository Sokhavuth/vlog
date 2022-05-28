#controllers/login/logout.py
import config
from bottle import response, redirect
 
def call():
    response.delete_cookie('userID', path='/', secret=config.kdict['SECRET_KEY'])
    response.delete_cookie('userRole', path='/', secret=config.kdict['SECRET_KEY'])
    redirect('/')