from models.client import Client
from models.db import db

def obtenerClientes():
    clients = Client.query.all()
    return [client.serialize() for client in clients]

def obtenerClientePorId(id):
    client = Client.query.get(id)
    if client:
        return client.serialize()
    else:
        return None
    
def crearCliente(data):
    cliente_nuevo = Client(**data)
    db.session.add(cliente_nuevo)
    db.session.commit()
    return cliente_nuevo.serialize(), 201
def borrarCliente(id):
    Cliente = Client.query.get(id)
    if Cliente:
        db.session.delete(Cliente)
        db.session.commit()
        return '', 204
    else:
        return None, 404