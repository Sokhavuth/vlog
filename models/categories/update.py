#models/categories/update.py
import config

def call(id):
    category_ref = config.mydb.collection("categories").document(id)
    doc_category = category_ref.get()

    if doc_category.exists:
        return doc_category.to_dict()