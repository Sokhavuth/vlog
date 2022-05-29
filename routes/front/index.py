#routes/frontend/index.py
import config
from .. import static
 
app = static.app
 
@app.route('/')
def index():
    from controllers.front import index
    return index.call()