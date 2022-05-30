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

    result = read.call(kdict['maxPosts'])
    kdict['items'] = result['categories']
    kdict['counter'] = result['counter']

    return template('base',data=kdict)