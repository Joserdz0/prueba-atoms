from flask import Blueprint, render_template, request
from models.product import Product
from utils.db import db 

products = Blueprint('products', __name__)

@products.route('/')
def index():
    return render_template('index.html')
@products.route('/new', methods=['POST'])
def addProduct():
    name = request.form['name']
    new_product = Product(name)
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

