import sqlalchemy
from flask import request
from flask_restful import Resource
from sqlalchemy import insert, update

from utilidades.Extactor import Extractor
from configuracion.conexion_bd import db_session
from entidades.entidad_categoria import ModeloCategoria


class RutaCategoriaById(Resource):

    def get(self, id_categoria):
        extractor = Extractor()
        resultado = extractor.extraer(ModeloCategoria, db_session, ModeloCategoria.id_categoria, id_categoria)
        return resultado


class RutaCategoriaIAE(Resource):

    def post(self):
        args = request.get_json()
        categoria = ModeloCategoria()
        categoria.set_valores(args['categoria'], args['sub_categoria'])
        db_session.add(categoria)
        db_session.commit()
        print(categoria.id_categoria)
        return args

    def put(self):
        args = request.get_json()
        categoria = db_session.query(ModeloCategoria).get(args['id_categoria'])
        categoria.set_valores(args['categoria'], args['sub_categoria'])
        db_session.commit()
        return args

    def delete(self):
        args = request.get_json()
        categoria = db_session.query(ModeloCategoria).get(args['id_categoria'])
        try:
            print(db_session.delete(categoria))
            db_session.commit()
            return {'id_eliminado': categoria.id_categoria}
        except:
            return {'id_eliminado': 'El id especificado no existe'}
