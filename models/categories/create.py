#models/categories/create.py
import uuid
from models import setDBconnection
from bottle import request

def call():
    id = uuid.uuid4().hex
    category = {
        'id': id,
        'title': request.forms.getunicode('title'),
        'thumb': request.forms.getunicode('thumb'),
        'date': request.forms.getunicode('datetime')
    }

    doc_ref = setDBconnection.db.collection('categories').document(id)
    doc_ref.set(category)