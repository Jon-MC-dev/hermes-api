from sqlalchemy import Column, Integer, String, PickleType, Float, ForeignKey
from configuracion.conexion_bd import Base


class ModeloProductos(Base):
    __tablename__ = "tbl_productos"

    id_producto = Column(Integer, primary_key=True)
    id_cooperativa = Column(Integer, ForeignKey('tbl_cooperativas.id_cooperativa'))
    id_categoria = Column(Integer, ForeignKey('tbl_categorias.id_categoria'))
    descripcion = Column(String(300), unique=False, nullable=False)
    precio = Column(Float, unique=False, nullable=False)
    fotografias = Column(PickleType, unique=False, nullable=False)
    activo = Column(Integer, unique=False, nullable=False)
