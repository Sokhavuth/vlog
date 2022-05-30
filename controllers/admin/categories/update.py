#controllers/admin/categories/update.py
import config
from copy import deepcopy
from bottle import template
from models.categories import read,update

def call(id):
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​កែប្រែជំពូក'
    kdict['route'] = '/admin/category'
    kdict['type'] = 'category'

    kdict['item'] = update.call(id)
    kdict['items'] = read.call(kdict['maxPosts'])

    return template('base',data=kdict)