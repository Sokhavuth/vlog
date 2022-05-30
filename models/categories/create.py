#models/categories/create.py
import uuid,config
from bottle import request

def call():
    if(request.forms.getunicode('id')):
        id = request.forms.getunicode('id')
    else:
        id = uuid.uuid4().hex
    category = {
        'id': id,
        'title': request.forms.getunicode('title'),
        'thumb': request.forms.getunicode('thumb'),
        'date': request.forms.getunicode('datetime'),
        'timestamp': config.firestore.SERVER_TIMESTAMP
    }

    category_ref = config.mydb.collection('categories').document(id)
    counter_ref = config.mydb.collection('counters').document('category')

    if(request.forms.getunicode('id')):
        category_ref.update(category)
    else:
        category_ref.set(category)
        counter_ref.update({'total': config.firestore.Increment(1)})
        