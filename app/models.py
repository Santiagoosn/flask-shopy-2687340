from . import db
from datetime import datetime


#Crear los modelos
class Cliente(db.Model):
    
 #definir los atributos 
     __tablename__="clientes"
     id = db.Column(db.Integer, primary_key = True)
     username = db.Column(db.String(120), 
                          nullable = True )
     password = db.Column(db.String(120), 
                          nullable = True)
     email = db.Column(db.String(120), 
                          nullable = True)
     
      #relaciones SQL alchemy
     ventas = db.relationship("Venta" ,
                              backref = "cliente" , 
                              lazy = "dynamic")
class Producto (db.Model):
     #definir los atributos
     __tablename__="productos"
     id = db.Column(db.Integer, primary_key = True)
     nombre = db.Column(db.String(120))
     precio = db.Column(db.Numeric(precision = 10, scale = 2))
     imagen = db.Column(db.String(200))

class Venta (db.Model):
     #definir los atributos
     __tablename__="ventas"
     id = db.Column(db.Integer, primary_key = True)
     fecha = db.Column(db.DateTime, 
                      default = datetime.utcnow)
    #clave foranea:
     cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))
   
    
    
class Detalle (db.Model):
     #definir los atributos
     __tablename__="detalles"
     id = db.Column(db.Integer, primary_key = True)

    #clave foranea:
     Producto_id = db.Column(db.Integer, 
                           db.ForeignKey('productos.id'))
     Venta_id = db.Column(db.Integer, 
                           db.ForeignKey('ventas.id'))
     cantidad = db.Column(db.Integer)