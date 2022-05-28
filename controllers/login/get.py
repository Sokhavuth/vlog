#controllers/login/get.py
import config
from copy import deepcopy
from bottle import template

def call():
    kdict = deepcopy(config.kdict)
    kdict['pageTitle'] = 'ទំព័រ​ចុះ​ឈ្មោះ'
    kdict['route'] = '/login'

    return template('base',data=kdict)
