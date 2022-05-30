#models/categories/read.py
import config
from models import setDBconnection as con

def call(amount):
    categories_ref = con.db.collection("categories")
    query = categories_ref.order_by("date",direction=con.firestore.Query.DESCENDING).limit(amount)

    results = query.get()
    categories = [category.to_dict() for category in results]
    
    return categories