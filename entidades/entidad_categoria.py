from sqlalchemy import Column, Integer, String, insert
from configuracion.conexion_bd import Base


class ModeloCategoria(Base):
    __tablename__ = "tbl_categorias"

    id_categoria = Column(Integer, primary_key=True)
    categoria = Column(String(45), unique=False, nullable=False)
    sub_categoria = Column(String(45), unique=True, nullable=False)

    def set_valores(self, categoria, sub_categoria):
        self.categoria=categoria
        self.sub_categoria=sub_categoria
