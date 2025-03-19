from flask import Blueprint, request, jsonify
import chromadb

users_bp = Blueprint("users", __name__)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
        "This is a document about mango",
        "cricket is the national sport of pakistan"
        
    ],
    ids=["id1", "id2", "id3", "id4"]
)


@users_bp.route("/", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})


@users_bp.route("/test", methods=["POST"])
def test(): 
    query = request.form.get('query') 
    results = collection.query(
        query_texts=[query], # Chroma will embed this for you
        n_results=2 # how many results to return
    )
    print(results)
    return jsonify(results) 