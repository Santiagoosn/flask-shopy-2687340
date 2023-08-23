#dependencia de flask
from flask import Flask

#dependencia de configuracion 
from .config import Config 

#dependencias de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate
from .mi_blueprint import mi_blueprint
from app.products import products
#dependencia a botstrap
from flask_bootstrap import Bootstrap

#crear el objeto flask
app = Flask(__name__)

#configuracion del objeto flask 
app.config.from_object(Config)

#Vincular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)


#Crear el objeto de modelos:
db = SQLAlchemy(app)

#Cear el objeto de migracion
migrate = Migrate(app, db)

#Crear objeto de bootstrap
bootstrap = Bootstrap(app)

#importar los modelos de .models
from .models import Cliente, Producto, Venta, Detalle