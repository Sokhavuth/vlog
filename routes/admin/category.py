#routes/admin/index.py
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