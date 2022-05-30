#controllers/admin/categories/read.py
import config
from copy import deepcopy
from bottle import template
from models.categories import read

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = '/admin/category'
    kdict['type'] = 'category'

    kdict['items'] = read.call(kdict['maxPosts'])

    return template('base',data=kdict)