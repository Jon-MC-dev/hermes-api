from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion.conexion_bd import Base


class ModeloPersona(Base):
    __tablename__ = "tbl_personas"

    id_persona = Column(Integer, primary_key=True)
    nombre_persona = Column(String(40), unique=False, nullable=False)
    ape_paterno = Column(String(40), unique=False, nullable=False)
    ape_materno = Column(String(40), unique=False, nullable=False)
    foto_perfil = Column(String(40), unique=True, nullable=False)
    id_usuario = Column(Integer, ForeignKey('tbl_usuarios.id_usuario'))

