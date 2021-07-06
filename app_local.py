from flask import Flask
from flask_restful import Api
from configuracion.conexion_bd import iniciar_base_datos


from rutas.hello_word import HolaMundo
from rutas.ruta_cooperativa import RutaCooperativaById, RutaCooperativaIAE
from rutas.ruta_persona import RutaPersona
from rutas.ruta_producto import RutaProductoById, RutaProductoIAE
from rutas.ruta_usuario import RutaUsuario
from rutas.rutas_categoria.ruta_categoria import RutaCategoriaById, RutaCategoriaIAE

app = Flask(__name__)
api = Api(app)
# worker python app.py
api.add_resource(HolaMundo, '/')
api.add_resource(RutaUsuario, '/usuario/<int:id_usuario>')
api.add_resource(RutaPersona, '/persona')
api.add_resource(RutaCategoriaById, '/categoria/<int:id_categoria>')  # buscar categorias
api.add_resource(RutaCategoriaIAE, '/categoria/IAE')
#
api.add_resource(RutaCooperativaById, '/cooperativa/<int:id_cooperativa>')
api.add_resource(RutaCooperativaIAE, '/cooperativa/IAE')
#
api.add_resource(RutaProductoById, '/producto/<int:id_producto>')
api.add_resource(RutaProductoIAE, '/producto/IAE')



if __name__ == '__main__':
    iniciar_base_datos()
    app.run(debug=True)