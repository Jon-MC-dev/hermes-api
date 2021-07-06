from flask_restful import Resource
from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult

from entidades.entidad_usuario import ModeloUsuario
from configuracion.conexion_bd import db_session


class RutaUsuario(Resource):
    def get(self, id_usuario):
        print("Hola que tal")
        try:
            if id_usuario == 0:
                usuarios = db_session.query(ModeloUsuario).all()
                list_usuarios = []
                for usuario in usuarios:
                    list_usuarios.append({'id_usuario': usuario.id_usuario, 'rol': usuario.rol,
                                          'nombre_usuario': usuario.nombre_usuario})
                return list_usuarios
            else:
                usuario: ChunkedIteratorResult = db_session.execute(
                    select(ModeloUsuario).where(ModeloUsuario.id_usuario == id_usuario))
                ##
                try:
                    usuario = usuario.all()[0][0]
                    print(usuario)
                    return {'id_usuario': usuario.id_usuario, 'rol': usuario.rol,
                            'nombre_usuario': usuario.nombre_usuario}
                except:
                    return {'id_usuario': 0, 'rol': 'No existe',
                            'nombre_usuario': 'No existe', 'error': 'El usuario especificado no existe'}
                ##
        except (RuntimeError, TypeError, NameError):
            print(TypeError)
            return {'NameError': NameError, 'id_usuario': id_usuario}
