#controllers/admin/categories/delete.py
import config
from bottle import redirect, request
from models.categories import delete

def call(id):
    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

    if(userRole == 'Admin'):
        delete.call(id)

    redirect('/admin/category')