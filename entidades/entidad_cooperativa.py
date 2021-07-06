from sqlalchemy import Column, Integer, String, Boolean
from configuracion.conexion_bd import Base


class ModeloCooperativa(Base):
    __tablename__ = "tbl_cooperativas"

    id_cooperativa = Column(Integer, primary_key=True)
    nombre_cooperativa = Column(String(40), unique=True, nullable=False)
    descripcion = Column(String(500), unique=False, nullable=False)
    foto_portada = Column(String(150), unique=False, nullable=False)
    estado_republica = Column(String(40), unique=False, nullable=False)
    activo = Column(Boolean, unique=False, nullable=False)
    numero_productores = Column(Integer, unique=False, nullable=False)
