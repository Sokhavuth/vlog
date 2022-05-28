#models/users/checkUser.py
import config
from .. import setDBconnection
 
def call(email):
    users_ref = setDBconnection.db.collection(u'users').where(u'email',u'==',email)
    users = users_ref.stream()

    for user in users:
        userEmail = user.get('email')
        if(userEmail == email):
            return user.to_dict()