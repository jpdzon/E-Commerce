from flask import Flask, render_template
from pymongo import MongoClient
from flask_login import LoginManager
from bson.objectid import ObjectId


def create_app():
    app = Flask(__name__, template_folder='template', static_folder='static')
    app.config['SECRET_KEY'] = 'asdcsdef'

    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]  

    app.db = db

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        from .models import UserMongo
        try:
            user_data = db.customers.find_one({"_id": ObjectId(user_id)})
            if user_data:
                return UserMongo(user_data)
        except:
            pass
        return None

    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Cart, Product, Order

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    return app