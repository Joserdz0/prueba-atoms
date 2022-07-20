import enum
from utils.db import db
class Product(db.Model):
    class MyStatus(enum.Enum):
        active = 1
        archived = 2
        draft = 3   
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    sku = db.Column(db.String(100),unique=True)
    images = db.Column(db.LargeBinary)
    tags = db.Column(db.String(1000))
    price = db.Column(db.Float)
    status = db.Column(db.Enum(MyStatus))
    size = db.Column(db.String(1000))
    created_at = db.Column(db.TIMESTAMP,server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = db.Column(db.TIMESTAMP,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    def __init__(self,name,sku,images,tags,price,status,size,created_at, updated_at):
        self.name = name
        self.sku = sku
        self.images = images
        self.tags = tags
        self.price = price
        self.status = status
        self.size = size
        self.created_at = created_at
        self.updated_at = updated_at