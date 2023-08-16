#dependencia de flask
from flask import Flask

#dependencia de configuracion 
from .config import Config 

#dependencias de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

#crear el objeto flask
app = Flask(__name__)

#configuracion del objeto flask 
app.config.from_object(Config)



#Crear el objeto de modelos:
db = SQLAlchemy(app)

#Cear el objeto de migracion
migrate = Migrate(app, db)

#importar los modelos de .models
from .models import Cliente, Producto, Venta, Detalle