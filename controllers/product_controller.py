from models.product import Products
from models.db import db

def obtenerProductos():
    productos = Products.query.all()
    return [producto.serialize() for producto in productos]

def obtenerProductoPorId(id):
    producto = Products.query.get(id)
    if producto:
        return producto.serialize()
    else:
        return None

def crearProducto(data):
    producto_nuevo = Products(**data)
    db.session.add(producto_nuevo)
    db.session.commit()
    return producto_nuevo.serialize(), 201

def borrarProducto(id):
    producto = Products.query.get(id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return '', 204
    else:
        return None, 404