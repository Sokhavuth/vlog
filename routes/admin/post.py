#routes/admin/post.py
from bottle import Bottle,redirect
from controllers.login import checkLogged

app = Bottle()

@app.route('/')
def getPost():
    if checkLogged.call():
        from controllers.admin.posts import read
        return read.call()
    else:
        redirect('/login')