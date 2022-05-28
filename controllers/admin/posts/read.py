#controllers/admin/post/read.py
import config
from copy import deepcopy
from bottle import template

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = '/admin/post'

    return template('base',data=kdict)