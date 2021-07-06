from flask import Flask
from flask_restful import Api
from rutas.rutas_categoria.ruta_categoria import RutaCategoriaById, RutaCategoriaIAE


from rutas.hello_word import HolaMundo
from rutas.ruta_persona import RutaPersona
from rutas.ruta_usuario import RutaUsuario

app = Flask(__name__)
api = Api(app)
# worker python app.py
api.add_resource(HolaMundo, '/')
api.add_resource(RutaUsuario, '/usuario/<int:id_usuario>')
api.add_resource(RutaPersona, '/persona')
api.add_resource(RutaCategoriaById, '/categoria/<int:id_categoria>')  # buscar categorias
api.add_resource(RutaCategoriaIAE, '/categoria/IAE')
#if __name__ == '__main__':
#    iniciar_base_datos()
#    app.run(debug=True)