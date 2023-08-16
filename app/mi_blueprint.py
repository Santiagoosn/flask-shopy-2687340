from flask import Blueprint

mi_blueprint = Blueprint('mi _blueprint',
                         __name__,
                         url_prefix='/ejemplo'
                         )

@mi_blueprint.route('/prueba')
def index():
    return "Hola, me encuentro en blueprint"
