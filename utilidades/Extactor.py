from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult

from entidades.entidad_categoria import ModeloCategoria


class Extractor:

    def extraer(self, claseModelo, db_session, id_elemento, id=0):
        retorno = dict()
        try:
            if id == 0:
                lista = db_session.query(claseModelo).all()
                list_generica = []
                for elemento in lista:
                    list_generica.append(elemento)
                print("---------- Primer caso ----------")
                retorno['tipo'] = 'lista'
                retorno['lista'] = list_generica
                retorno['error'] = ''
                return retorno
            else:
                resultado: ChunkedIteratorResult = db_session.execute(
                    select(claseModelo).where(id_elemento == id))
                try:
                    elemento = resultado.all()[0][0]
                    print("---------- Segundo caso ----------")
                    retorno['tipo'] = 'elemento_unico'
                    retorno['elemento_unico'] = elemento
                    retorno['error'] = ''
                    return retorno
                except:
                    print("---------- Tercer caso ----------")
                    retorno['tipo'] = 'error'
                    retorno['error'] = 'Inexistente'
                    return retorno
                ##
        except (RuntimeError, TypeError, NameError):
            # print(TypeError)
            print("---------- Cuarto caso ----------")
            retorno['tipo'] = 'error'
            retorno['error'] = NameError
            return retorno
