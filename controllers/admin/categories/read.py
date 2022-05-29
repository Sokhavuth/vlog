#controllers/admin/categories/read.py
import config
from copy import deepcopy
from bottle import template

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = '/admin/category'

    return template('base',data=kdict)