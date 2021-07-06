import sqlalchemy
from flask import request
from flask_restful import Resource

from utilidades.Extactor import Extractor
from configuracion.conexion_bd import db_session
from entidades.entidad_producto import ModeloProducto


class RutaProductoById(Resource):

    def get(self, id_producto):
        extractor = Extractor()
        resultado = extractor.extraer(ModeloProducto, db_session, ModeloProducto.id_producto, id_producto)
        if resultado['tipo'] != 'error':
            if resultado['tipo'] == 'lista':
                lista_productos = []
                for ele in resultado['lista']:
                    lista_productos.append(
                        {'id_producto': ele.id_producto, 'id_cooperativa': ele.id_cooperativa,
                         'id_categoria': ele.id_categoria, 'descripcion': ele.descripcion,
                         'precio': ele.precio, 'fotografias': ele.fotografias,
                         'activo': ele.activo})
                resultado['lista'] = lista_productos
            else:
                ele = resultado['elemento_unico']
                resultado['elemento_unico'] = {'id_producto': ele.id_producto, 'id_cooperativa': ele.id_cooperativa,
                                               'id_categoria': ele.id_categoria, 'descripcion': ele.descripcion,
                                               'precio': ele.precio, 'fotografias': ele.fotografias,
                                               'activo': ele.activo}
        return resultado


class RutaProductoIAE(Resource):

    def post(self):
        args = request.get_json()
        producto = ModeloProducto()
        producto.set_valores(args['id_cooperativa'], args['id_categoria'], args['descripcion'],
                                args['precio'], args['fotografias'], args['activo'])
        db_session.add(producto)
        db_session.commit()
        # db_session.close()
        args['id_producto'] = producto.id_producto
        return args

    def put(self):
        args = request.get_json()
        try:
            producto = db_session.query(ModeloProducto).get(args['id_producto'])
            producto.set_valores(args['id_cooperativa'], args['id_categoria'], args['descripcion'],
                                 args['precio'], args['fotografias'], args['activo'])
            db_session.commit()
            return args
        except:
            return {'error': 'El id especificado no existe'}

    def delete(self):
        args = request.get_json()
        producto = db_session.query(ModeloProducto).get(args['id_producto'])
        try:
            print(db_session.delete(producto))
            db_session.commit()
            return {'id_eliminado': producto.id_producto}
        except:
            return {'error': 'El id especificado no existe'}
