#routes/static.py
import config
from bottle import Bottle, static_file
 
app = Bottle()
 
@app.route('/static/images/<filename>')
def loadImage(filename):
    return static_file(filename, root='./public/images')
 
@app.route('/static/styles/<filename>')
def loadStyle(filename):
    return static_file(filename, root='./public/styles')
 
@app.route('/static/scripts/<filename>')
def loadScript(filename):
    return static_file(filename, root='./public/scripts')
 
@app.route('/static/scripts/ckeditor/<filename>')
def loadCKEditorScript(filename):
    return static_file(filename, root='./public/scripts/ckeditor')
 
@app.route('/static/fonts/<filename>')
def loadFont(filename):
    return static_file(filename, root='./public/fonts')
 
@app.route('/static/uploads/<filename>')
def upload(filename):
    return static_file(filename, root='./public/uploads')