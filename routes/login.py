#routes/login.py
from bottle import Bottle,redirect
from controllers.login import checkLogged

app = Bottle()

@app.route('/')
def getForm():
    if not checkLogged.call():
        redirect('/admin/post')
    else:
        from controllers.login import get
        return get.call()

@app.route('/',method='post')
def checkUser():
    from controllers.login import checkUser
    return checkUser.call()