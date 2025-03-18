from flask import Flask 
from flask_cors import CORS 
from dotenv import load_dotenv 
import os 

def create_app(): 
    # Load environment variables 
    load_dotenv()
    
    # Initialize Flask App 
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object("books_rag_app.config.Config")

    # Enable CORS
    CORS(app)

    # Register Blueprints
    from books_rag_app.routes.user import users_bp
    from books_rag_app.routes.post import posts_bp

    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(posts_bp, url_prefix="/api/posts")

    return app