#routes/frontend/index.py
import config
from .. import static
 
app = static.app
 
@app.route('/')
def index():
    return config.kdict['siteTitle']