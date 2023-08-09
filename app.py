#dependencia de flask
from flask import Flask, render_template

#dependencias de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

#Dependencia para fecha y hora de sistema
from datetime import datetime 
#Dependencias de wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#crear el objeto flask
app = Flask(__name__)

#definir la cadena de conexion ("conectionstring")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3311/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'FICHA_2687340'

#Crear el objeto de modelos:
db = SQLAlchemy(app)

#Cear el objeto de migracion
migrate = Migrate(app, db)

#Crear formulario de registro de productos
class ProductosForm(FlaskForm):
     nombre = StringField('nombre_producto')
     precio = StringField('precio_producto')
     submit = SubmitField('registrar Producto')
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
    
    #rutas:
@app.route('/productos', 
           methods = ['GET','POST'])
def nuevo_producto():
     form = ProductosForm()
     if form.validate_on_submit():
          #creamos un nuevo producto
          p = Producto(nombre = form.nombre.data, 
                       precio = form.precio.data)
          db.session.add(p)
          db.session.commit()
          return "producto registrado"
     return render_template('nuevoproducto.html', 
                     form = form)
     