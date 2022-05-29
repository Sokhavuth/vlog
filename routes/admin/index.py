#routes/admin/index.py
from bottle import Bottle
from . import post
from . import category

app = Bottle()

app.mount('/post',post.app)
app.mount('/category',category.app)