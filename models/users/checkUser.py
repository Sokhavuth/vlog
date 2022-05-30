#models/users/checkUser.py
import config
 
def call(email):
    users_ref = config.mydb.collection(u'users').where(u'email',u'==',email)
    users = users_ref.stream()

    for user in users:
        userEmail = user.get('email')
        if(userEmail == email):
            return user.to_dict()