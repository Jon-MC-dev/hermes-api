from flask_restful import Resource
from entidades.entidad_usuario import ModeloUsuario
from configuracion.conexion_bd import db_session


class RutaUsuario(Resource):
    def get(self, id_usuario):
        print("Hola que tal")
        try:
            if id_usuario==0:
                usuarios = db_session.query(ModeloUsuario).all()
                list_usuarios = []
                for usuario in usuarios:
                    list_usuarios.append({'id_usuario': usuario.id_usuario, 'rol': usuario.rol, 'nombre_usuario': usuario.nombre_usuario})
                return list_usuarios
            else:
                return {'Mensaje': 'en construccion'}
        except (RuntimeError, TypeError, NameError):
            print(TypeError)
            return {'hola': 'mundo', 'id_usuario': id_usuario}
