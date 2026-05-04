from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.product import Products

products = Blueprint('products', __name__)

@products.route('/api/products')
def get_products():
    products = Products.query.all()
    return jsonify([product.serialize() for product in products])