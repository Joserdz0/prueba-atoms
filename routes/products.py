from flask import Blueprint, render_template, request
from models.product import Product
from utils.db import db 

products = Blueprint('products', __name__)

@products.route('/')
def index():
    return render_template('index.html')
@products.route('/new', methods=['POST'])
def addProduct():
    #Tengo que ver como arreglar el JSON que recibo
    request_data = request.get_json()
    name = request_data["name"]
    sku = request_data["sku"]
    images = request_data["sku"]
    tags = request_data["tags"]
    price = request_data["price"]
    status = request_data["status"]
    size = request_data["size"]
    created_at = ""
    updated_at = ""
    new_product = Product(name,sku,images,tags,price,status,size,created_at,updated_at)
    db.session.add(new_product)
    db.session.commit()
    return "Creando nuevos"
@products.route('/update')
def updateProduct():
    return "Actualizando nuevos"
@products.route('/delete')
def deleteProduct():
    return "eliminando nuevos"
@products.route('/delete')
def selectProduct():
    return "buscar nuevos"

