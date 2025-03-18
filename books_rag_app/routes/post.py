from flask import Blueprint, jsonify

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/", methods=["GET"])
def get_posts():
    return jsonify({"posts": ["Post 1", "Post 2", "Post 3"]})
