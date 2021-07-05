from sqlalchemy import Column, Integer, String

from configuracion.conexion_bd import Base


class ModeloUsuario(Base):
    __tablename__ = "tbl_usuarios"

    id_usuario = Column(Integer, primary_key=True)
    # ROL_NORMAL, ROL_COOPERATIVA, ROL_ADMIN_INFORMACION, ROL_VISOR_PEDIDOS, ROL_ADMIN
    rol = Column(String(40), unique=False, nullable=False)
    nombre_usuario = Column(String(40), unique=True, nullable=False)
    contrasena = Column(String(40), unique=True, nullable=False)
