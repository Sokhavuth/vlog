#controllers/login/checkUser.py
import config,bcrypt
from copy import deepcopy
from bottle import template, request, response, redirect
from models.users import checkUser
 
def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ចុះ​ឈ្មោះ'
 
    password = request.forms.getunicode('password')
    email = request.forms.getunicode('email')
    
    user = checkUser.call(email)
    
    if user:
        if(bcrypt.checkpw(password.encode('utf-8'), user['password'])):
            kdict["pageTitle"] = 'ទំព័រ​ការផ្សាយ'
            kdict['route'] = '/admin/post'
            response.set_cookie('userID', user['userID'], path='/', secret=kdict['SECRET_KEY'])
            response.set_cookie('userRole', user['role'], path='/', secret=kdict['SECRET_KEY'])
            return redirect('/admin/post')
        else:
            kdict['message'] = 'ពាក្យ​សំងាត់របស់អ្នក​​មិន​ត្រឹមត្រូវ​ទេ!'
            kdict['route'] = '/login'
            return template('base', data=kdict)
    else:
        kdict['message'] = 'Email របស់​អ្នក​មិន​ត្រឹមត្រូវ​ទេ!'
        kdict['route'] = '/login'
        return template('base', data=kdict)