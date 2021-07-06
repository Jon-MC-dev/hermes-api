import sqlalchemy
from flask import request
from flask_restful import Resource

from utilidades.Extactor import Extractor
from configuracion.conexion_bd import db_session
from entidades.entidad_cooperativa import ModeloCooperativa


class RutaCooperativaById(Resource):

    def get(self, id_cooperativa):
        extractor = Extractor()
        resultado = extractor.extraer(ModeloCooperativa, db_session, ModeloCooperativa.id_cooperativa, id_cooperativa)
        if resultado['tipo'] != 'error':
            if resultado['tipo'] == 'lista':
                lista_cooperativas = []
                for ele in resultado['lista']:
                    # id_cooperativa, nombre_cooperativa, descripcion, foto_portada, estado_republica, activo, numero_productores
                    lista_cooperativas.append(
                        {'id_cooperativa': ele.id_cooperativa, 'nombre_cooperativa': ele.nombre_cooperativa,
                         'descripcion': ele.descripcion, 'foto_portada': ele.foto_portada,
                         'estado_republica': ele.estado_republica, 'activo': ele.activo,
                         'numero_productores': ele.numero_productores})
                resultado['lista'] = lista_cooperativas
            else:
                ele = resultado['elemento_unico']
                resultado['elemento_unico'] = {'id_cooperativa': ele.id_cooperativa,
                                               'nombre_cooperativa': ele.nombre_cooperativa,
                                               'descripcion': ele.descripcion, 'foto_portada': ele.foto_portada,
                                               'estado_republica': ele.estado_republica, 'activo': ele.activo,
                                               'numero_productores': ele.numero_productores}
        return resultado


class RutaCooperativaIAE(Resource):

    def post(self):
        args = request.get_json()
        cooperativa = ModeloCooperativa()
        cooperativa.set_valores(args['nombre_cooperativa'], args['descripcion'], args['foto_portada'], args['estado_republica'], args['activo'], args['numero_productores'])
        db_session.add(cooperativa)
        db_session.commit()
        args['id_cooperativa'] = cooperativa.id_cooperativa
        return args

    def put(self):
        args = request.get_json()
        try:
            cooperativa = db_session.query(ModeloCooperativa).get(args['id_cooperativa'])
            cooperativa.set_valores(args['nombre_cooperativa'], args['descripcion'], args['foto_portada'], args['estado_republica'], args['activo'], args['numero_productores'])
            db_session.commit()
            return args
        except:
            return {'error': 'El id especificado no existe'}


    def delete(self):
        args = request.get_json()
        cooperativa = db_session.query(ModeloCooperativa).get(args['id_cooperativa'])
        try:
            print(db_session.delete(cooperativa))
            db_session.commit()
            return {'id_eliminado': cooperativa.id_cooperativa}
        except:
            return {'error': 'El id especificado no existe'}
