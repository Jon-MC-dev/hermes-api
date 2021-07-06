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
        print(ModeloCategoria)
        resultado = extractor.extraer(ModeloCategoria, db_session, ModeloCategoria.id_categoria, id_categoria)
        if resultado['tipo'] != 'error':
            if resultado['tipo'] == 'lista':
                lista_categorias = []
                for elemento in resultado['lista']:
                    lista_categorias.append({'id_categoria': elemento.id_categoria, 'categoria': elemento.categoria,
                                             'sub_categoria': elemento.sub_categoria})
                resultado['lista'] = lista_categorias
            else:
                elemento = resultado['elemento_unico']
                resultado['elemento_unico'] = {'id_categoria': elemento.id_categoria, 'categoria': elemento.categoria,
                                               'sub_categoria': elemento.sub_categoria}

        return resultado


class RutaCategoriaIAE(Resource):

    def post(self):
        args = request.get_json()
        categoria = ModeloCategoria()
        categoria.set_valores(args['categoria'], args['sub_categoria'])
        db_session.add(categoria)
        db_session.commit()
        args['id_categoria'] = categoria.id_categoria
        return args

    def put(self):
        args = request.get_json()
        try:
            categoria = db_session.query(ModeloCategoria).get(args['id_categoria'])
            categoria.set_valores(args['categoria'], args['sub_categoria'])
            db_session.commit()
            return args
        except:
            return {'error': 'El id especificado no existe'}


    def delete(self):
        args = request.get_json()
        categoria = db_session.query(ModeloCategoria).get(args['id_categoria'])
        try:
            print(db_session.delete(categoria))
            db_session.commit()
            return {'id_eliminado': categoria.id_categoria}
        except:
            return {'error': 'El id especificado no existe'}
