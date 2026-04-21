from datetime import datetime
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserMongo(UserMixin):
    def __init__(self, customer_doc):
        self.id = str(customer_doc.get('_id'))
        self.email = customer_doc.get('email')
        self.username = customer_doc.get('username')
        self.password_hash = customer_doc.get('password')
    
    def get_id(self):
        return self.id

class Customer:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.date_joined = datetime.utcnow()

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "email": self.email,
            "username": self.username,
            "password_hash": self.password_hash,
            "date_joined": self.date_joined
        }
class Product:
    def __init__(self, name, current_price, previous_price, stock, picture, flash_sale=False):
        self.product_name = name
        self.current_price = current_price
        self.previous_price = previous_price
        self.in_stock = stock
        self.product_picture = picture
        self.flash_sale = flash_sale
        self.date_added = datetime.utcnow()

    def to_dict(self):
        return {
            "product_name": self.product_name,
            "current_price": self.current_price,
            "previous_price": self.previous_price,
            "in_stock": self.in_stock,
            "product_picture": self.product_picture,
            "flash_sale": self.flash_sale,
            "date_added": self.date_added
        }
class Cart:
    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = ObjectId(customer_id)
        self.product_id = ObjectId(product_id)
        self.quantity = quantity

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }
class Order:
    def __init__(self, customer_id, product_id, quantity, price, status, payment_id):
        self.customer_id = ObjectId(customer_id)
        self.product_id = ObjectId(product_id)
        self.quantity = quantity
        self.price = price
        self.status = status
        self.payment_id = payment_id

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status,
            "payment_id": self.payment_id
        }