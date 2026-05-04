from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.client import Client

client = Blueprint('client', __name__)

@client.route('/api/clients')
def get_client():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients])