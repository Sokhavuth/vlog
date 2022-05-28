#index.py
from routes import login
from routes.front import index

app = index.app
app.mount('/login', login.app)

import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
   app.run(host='localhost', port=7000, debug=True, reloader=True)