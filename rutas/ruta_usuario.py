from flask_restful import Resource
from entidades.usuario import ModeloUsuario
from configuracion.conexion_bd import db_session

class RutaUsuario(Resource):
    def get(self):
        print("Hola que tal")
        try:
            usuario = db_session.query(ModeloUsuario).all()[0]
            print(usuario.nombre)
        except:
            pass
        return {'hola': 'mundo'}
