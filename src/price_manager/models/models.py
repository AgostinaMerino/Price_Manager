from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from price_manager.database.connection import Base
from price_manager.database.connection import engine


class CategoriaModel(Base):
  """Modelo ORM para categorías."""

  __tablename__ = "categorias"

  id = Column(Integer, primary_key=True)
  nombre = Column(String(100), nullable=False)


class ProveedorModel(Base):
  """Modelo ORM para proveedores."""

  __tablename__ = "proveedores"

  id = Column(Integer, primary_key=True)
  nombre = Column(String(100), nullable=False)
  contacto = Column(String(150), nullable=False)


class MonedaModel(Base):
  """Modelo ORM para monedas."""

  __tablename__ = "monedas"

  id = Column(Integer, primary_key=True)
  nombre = Column(String(3), nullable=False)


class TipoCotizacionModel(Base):
  """Modelo ORM para tipos de cotización."""

  __tablename__ = "tipos_cotizacion"

  id = Column(Integer, primary_key=True)
  nombre = Column(String(100), nullable=False)


class ProductoModel(Base):
  """Modelo ORM para productos."""

  __tablename__ = "productos"

  id = Column(Integer, primary_key=True)
  nombre = Column(String(100), nullable=False)
  descripcion = Column(String(255), nullable=False)
  precio_valor = Column(Float, nullable=False)
  precio_fecha = Column(Date, nullable=False)

  moneda_id = Column(
    Integer,
    ForeignKey("monedas.id"),
    nullable=False,
  )

  categoria_id = Column(
    Integer,
    ForeignKey("categorias.id"),
    nullable=False,
  )

  proveedor_id = Column(
    Integer,
    ForeignKey("proveedores.id"),
    nullable=False,
  )


class StockModel(Base):
  """Modelo ORM para stock."""

  __tablename__ = "stocks"

  producto_id = Column(
    Integer,
    ForeignKey("productos.id"),
    primary_key=True,
  )

  cantidad = Column(Integer, nullable=False)


class CotizacionDolarModel(Base):
  """Modelo ORM para cotizaciones del dólar."""

  __tablename__ = "cotizaciones_dolar"

  id = Column(
    Integer,
    primary_key=True,
    autoincrement=True,
  )

  valor = Column(Float, nullable=False)
  fecha = Column(Date, nullable=False)

  tipo_id = Column(
    Integer,
    ForeignKey("tipos_cotizacion.id"),
    nullable=False,
  )


def crear_tablas() -> None:
  """Crea todas las tablas del sistema."""

  Base.metadata.create_all(bind=engine)
