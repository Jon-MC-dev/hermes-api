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

    def set_valores(self, nombre_cooperativa, descripcion, foto_portada, estado_republica, activo, numero_productores):
        self.nombre_cooperativa = nombre_cooperativa
        self.descripcion = descripcion
        self.foto_portada = foto_portada
        self.estado_republica = estado_republica
        self.activo = activo
        self.numero_productores = numero_productores
