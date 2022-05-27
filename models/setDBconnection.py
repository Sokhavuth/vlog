#models/setConnection.py
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bottle import request

cred = credentials.Certificate('credential.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
request.mydb = db