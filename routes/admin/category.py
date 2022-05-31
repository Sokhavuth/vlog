#routes/admin/category.py
from bottle import Bottle,redirect
from controllers.login import checkLogged

app = Bottle()

@app.route('/')
def readCategory():
    if checkLogged.call():
        from controllers.admin.categories import read
        return read.call()
    else:
        redirect('/login')

@app.route('/',method='post')
def createCategory():
    if checkLogged.call():
        from controllers.admin.categories import create
        return create.call()
    else:
        redirect('/login')

@app.route('/edit/<id>')
def editCategory(id):
    if checkLogged.call():
        from controllers.admin.categories import update
        return update.call(id)
    else:
        redirect('/login')

@app.route('/delete/<id>')
def deleteCategory(id):
    if checkLogged.call():
        from controllers.admin.categories import delete
        return delete.call(id)
    else:
        redirect('/login')