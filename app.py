from flask import Flask
from flask_restful import Api
from configuracion.conexion_bd import iniciar_base_datos


from rutas.hello_word import HolaMundo
from rutas.ruta_persona import RutaPersona
from rutas.ruta_usuario import RutaUsuario

app = Flask(__name__)
api = Api(app)
# worker python app.py
api.add_resource(HolaMundo, '/')
api.add_resource(RutaUsuario, '/usuario')
api.add_resource(RutaPersona, '/persona')

if __name__ == '__main__':
    iniciar_base_datos()
    app.run(debug=True)