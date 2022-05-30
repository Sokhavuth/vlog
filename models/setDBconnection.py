#models/setDBConnection.py
import config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('credential.json')
firebase_admin.initialize_app(cred)

config.mydb = firestore.client()
config.firestore = firestore