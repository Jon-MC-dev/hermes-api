from flask_restful import Resource

from entidades.entidad_persona import ModeloPersona
from configuracion.conexion_bd import db_session

class RutaPersona(Resource):
    def get(self):
        print("Hola que tal")
        try:
            persona = db_session.query(ModeloPersona).all()[0]
            print(persona.nombre_persona)
        except:
            pass
        return {'hola': 'mundo'}
