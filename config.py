#config.py
import os
#pip install python-dotenv
from dotenv import load_dotenv
 
load_dotenv()
kdict = {}

kdict['SECRET_KEY'] = os.environ.get('SECRET_KEY')
kdict['siteTitle'] = 'Khmer Web Vlog'
kdict['pageTitle'] = 'ទំព័រ​ដ់ើម'
kdict['message'] = ''
kdict['maxPosts'] = 10