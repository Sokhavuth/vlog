#models/categories/read.py
import config

def call(amount):
    categories_ref = config.mydb.collection("categories")
    query = categories_ref.order_by(
        "date",direction=config.firestore.Query.DESCENDING).limit(amount)

    results = query.get()
    categories = [category.to_dict() for category in results]

    counter_ref = config.mydb.collection("counters").document('category').get()
    if counter_ref.exists:
        counter = counter_ref.to_dict()
    
    return {'categories':categories, 'counter':counter}