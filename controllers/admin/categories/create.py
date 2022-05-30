#controllers/admin/categories/create.py
import config
from copy import deepcopy
from bottle import redirect,request
from models.categories import create

def call():
    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

    if(userRole == 'Admin'):
        create.call()

    redirect('/admin/category')