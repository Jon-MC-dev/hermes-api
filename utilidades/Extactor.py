from sqlalchemy import select
from sqlalchemy.engine import ChunkedIteratorResult


class Extractor:

    def extraer(self, claseModelo, db_session, id_elemento, id=0):
        try:
            if id == 0:
                lista = db_session.query(claseModelo).all()
                list_generica = []
                for elemento in lista:
                    list_generica.append(elemento)
                print("---------- Primer caso ----------")
                return list_generica
            else:
                resultado: ChunkedIteratorResult = db_session.execute(
                    select(claseModelo).where(id_elemento == id))
                try:
                    elemento = resultado.all()[0][0]
                    print("---------- Segundo caso ----------")
                    return elemento
                except:
                    print("---------- Tercer caso ----------")
                    return {'error': 'No existe'}
                ##
        except (RuntimeError, TypeError, NameError):
            print(TypeError)
            print("---------- Cuarto caso ----------")
            return {'NameError': NameError, 'id': id}
