#controllers/login/createRootUser.py
#pip install bcrypt
import uuid, config,bcrypt
from models import setDBconnection
 
def call():
    password = b"xxxxxxxxx"
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
 
    user = { 
        "userID": uuid.uuid4().hex, 
        "email": "root@khmerweb.app",
        "username": "root",
        "password": hashedPassword,
        "role":"Admin",
        "thumb":"",
        "info":"",
        "video":"",
        "date":""
     }
 
    doc_ref = setDBconnection.db.collection('users').document('root user')
    doc_ref.set(user)