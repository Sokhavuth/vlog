#routes/admin/category.py
from bottle import Bottle,redirect
from controllers.login import checkLogged

app = Bottle()

@app.route('/')
def getCategory():
    if checkLogged.call():
        from controllers.admin.categories import read
        return read.call()
    else:
        redirect('/login')

@app.route('/',method='post')
def postCategory():
    if checkLogged.call():
        from controllers.admin.categories import create
        return create.call()
    else:
        redirect('/login')