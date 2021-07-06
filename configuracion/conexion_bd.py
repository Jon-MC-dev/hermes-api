from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql://ubn9fnsnawvxiqbu:BivOg9P4Wx7EHUa1HS2z@bd2wuulpg5gelrwzim6x-mysql.services.clever-cloud.com:3306/bd2wuulpg5gelrwzim6x', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def iniciar_base_datos():
    from entidades.entidad_usuario import ModeloUsuario
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Pruevas
    #usuarios = ModeloUsuario()
    #usuarios.nombre="Jonathan"
    #usuarios.apellido="Morales"
    #db_session.add(usuarios)

    #db_session.commit()
