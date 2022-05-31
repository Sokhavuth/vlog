#models/categories/delete.py
import config

def call(id):
    config.mydb.collection(u'categories').document(id).delete()
    counter_ref = config.mydb.collection('counters').document('category')
    counter_ref.update({'total': config.firestore.Increment(-1)})