#index.py
from routes.frontend import index
from models import setDBconnection

app = index.app

import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
   app.run(host='localhost', port=7000, debug=True, reloader=True)