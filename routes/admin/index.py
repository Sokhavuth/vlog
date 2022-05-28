#routes/admin/index.py
from bottle import Bottle,redirect
from controllers.login import checkLogged

app = Bottle()

@app.route('/post')
def index():
    if checkLogged.call():
        from controllers.admin.posts import read
        return read.call()
    else:
        redirect('/login')