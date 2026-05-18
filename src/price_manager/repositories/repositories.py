import datetime
from typing import List, Optional

from price_manager.database.connection import obtener_sesion
from price_manager.entities.entities import (
  Categoria,
  CotizacionDolar,
  Moneda,
  Precio,
  Producto,
  Proveedor,
  Stock,
  TipoCotizacion,
)
from price_manager.models.models import (
  CategoriaModel,
  CotizacionDolarModel,
  MonedaModel,
  ProductoModel,
  ProveedorModel,
  StockModel,
  TipoCotizacionModel,
)


class RepositorioCategoria:
  """Repositorio SQLAlchemy para categorías."""

  def crear(self, categoria: Categoria) -> Categoria:
    with obtener_sesion() as session:
      model = CategoriaModel(id=categoria.id, nombre=categoria.nombre)
      session.add(model)
    return categoria

  def leer_por_id(self, id: int) -> Optional[Categoria]:
    with obtener_sesion() as session:
      model = session.get(CategoriaModel, id)
      if model is None:
        return None
      return Categoria(id=model.id, nombre=model.nombre)

  def leer_todos(self) -> List[Categoria]:
    with obtener_sesion() as session:
      modelos = session.query(CategoriaModel).all()
      return [Categoria(id=m.id, nombre=m.nombre) for m in modelos]

  def actualizar(self, categoria: Categoria) -> Categoria:
    with obtener_sesion() as session:
      model = session.get(CategoriaModel, categoria.id)
      if model is None:
        raise ValueError("No existe una entidad con ese ID.")
      model.nombre = categoria.nombre
    return categoria

  def eliminar(self, id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(CategoriaModel, id)
      if model is None:
        return False
      session.delete(model)
      return True


class RepositorioProveedor:
  """Repositorio SQLAlchemy para proveedores."""

  def crear(self, proveedor: Proveedor) -> Proveedor:
    with obtener_sesion() as session:
      model = ProveedorModel(
        id=proveedor.id,
        nombre=proveedor.nombre,
        contacto=proveedor.contacto,
      )
      session.add(model)
    return proveedor

  def leer_por_id(self, id: int) -> Optional[Proveedor]:
    with obtener_sesion() as session:
      model = session.get(ProveedorModel, id)
      if model is None:
        return None
      return Proveedor(
        id=model.id,
        nombre=model.nombre,
        contacto=model.contacto,
      )

  def leer_todos(self) -> List[Proveedor]:
    with obtener_sesion() as session:
      modelos = session.query(ProveedorModel).all()
      return [
        Proveedor(id=m.id, nombre=m.nombre, contacto=m.contacto)
        for m in modelos
      ]

  def actualizar(self, proveedor: Proveedor) -> Proveedor:
    with obtener_sesion() as session:
      model = session.get(ProveedorModel, proveedor.id)
      if model is None:
        raise ValueError("No existe una entidad con ese ID.")
      model.nombre = proveedor.nombre
      model.contacto = proveedor.contacto
    return proveedor

  def eliminar(self, id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(ProveedorModel, id)
      if model is None:
        return False
      session.delete(model)
      return True


class RepositorioMoneda:
  """Repositorio SQLAlchemy para monedas."""

  def crear(self, moneda: Moneda) -> Moneda:
    with obtener_sesion() as session:
      model = MonedaModel(id=moneda.id, nombre=moneda.nombre)
      session.add(model)
    return moneda

  def leer_por_id(self, id: int) -> Optional[Moneda]:
    with obtener_sesion() as session:
      model = session.get(MonedaModel, id)
      if model is None:
        return None
      return Moneda(id=model.id, nombre=model.nombre)

  def leer_todos(self) -> List[Moneda]:
    with obtener_sesion() as session:
      modelos = session.query(MonedaModel).all()
      return [Moneda(id=m.id, nombre=m.nombre) for m in modelos]

  def actualizar(self, moneda: Moneda) -> Moneda:
    with obtener_sesion() as session:
      model = session.get(MonedaModel, moneda.id)
      if model is None:
        raise ValueError("No existe una entidad con ese ID.")
      model.nombre = moneda.nombre
    return moneda

  def eliminar(self, id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(MonedaModel, id)
      if model is None:
        return False
      session.delete(model)
      return True


class RepositorioTipoCotizacion:
  """Repositorio SQLAlchemy para tipos de cotización."""

  def crear(self, tipo: TipoCotizacion) -> TipoCotizacion:
    with obtener_sesion() as session:
      model = TipoCotizacionModel(id=tipo.id, nombre=tipo.nombre)
      session.add(model)
    return tipo

  def leer_por_id(self, id: int) -> Optional[TipoCotizacion]:
    with obtener_sesion() as session:
      model = session.get(TipoCotizacionModel, id)
      if model is None:
        return None
      return TipoCotizacion(id=model.id, nombre=model.nombre)

  def leer_todos(self) -> List[TipoCotizacion]:
    with obtener_sesion() as session:
      modelos = session.query(TipoCotizacionModel).all()
      return [TipoCotizacion(id=m.id, nombre=m.nombre) for m in modelos]

  def actualizar(self, tipo: TipoCotizacion) -> TipoCotizacion:
    with obtener_sesion() as session:
      model = session.get(TipoCotizacionModel, tipo.id)
      if model is None:
        raise ValueError("No existe una entidad con ese ID.")
      model.nombre = tipo.nombre
    return tipo

  def eliminar(self, id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(TipoCotizacionModel, id)
      if model is None:
        return False
      session.delete(model)
      return True


class RepositorioProducto:
  """Repositorio SQLAlchemy para productos."""

  def crear(self, producto: Producto) -> Producto:
    with obtener_sesion() as session:
      model = ProductoModel(
        id=producto.id,
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio_valor=producto.precio.valor,
        precio_fecha=producto.precio.fecha,
        moneda_id=producto.precio.moneda.id,
        categoria_id=producto.categoria.id,
        proveedor_id=producto.proveedor.id,
      )
      session.add(model)
    return producto

  def _convertir_a_entidad(
    self,
    producto: ProductoModel,
    moneda: MonedaModel,
    categoria: CategoriaModel,
    proveedor: ProveedorModel,
  ) -> Producto:
    moneda_entidad = Moneda(id=moneda.id, nombre=moneda.nombre)

    precio = Precio(
      valor=producto.precio_valor,
      moneda=moneda_entidad,
      fecha=producto.precio_fecha,
    )

    categoria_entidad = Categoria(
      id=categoria.id,
      nombre=categoria.nombre,
    )

    proveedor_entidad = Proveedor(
      id=proveedor.id,
      nombre=proveedor.nombre,
      contacto=proveedor.contacto,
    )

    return Producto(
      id=producto.id,
      nombre=producto.nombre,
      descripcion=producto.descripcion,
      precio=precio,
      categoria=categoria_entidad,
      proveedor=proveedor_entidad,
    )

  def leer_por_id(self, id: int) -> Optional[Producto]:
    with obtener_sesion() as session:
      producto = session.get(ProductoModel, id)

      if producto is None:
        return None

      moneda = session.get(MonedaModel, producto.moneda_id)
      categoria = session.get(CategoriaModel, producto.categoria_id)
      proveedor = session.get(ProveedorModel, producto.proveedor_id)

      return self._convertir_a_entidad(
        producto,
        moneda,
        categoria,
        proveedor,
      )

  def leer_todos(self) -> List[Producto]:
    with obtener_sesion() as session:
      productos = session.query(ProductoModel).all()
      resultado = []

      for producto in productos:
        moneda = session.get(MonedaModel, producto.moneda_id)
        categoria = session.get(CategoriaModel, producto.categoria_id)
        proveedor = session.get(ProveedorModel, producto.proveedor_id)

        resultado.append(
          self._convertir_a_entidad(
            producto,
            moneda,
            categoria,
            proveedor,
          )
        )

      return resultado

  def actualizar(self, producto: Producto) -> Producto:
    with obtener_sesion() as session:
      model = session.get(ProductoModel, producto.id)

      if model is None:
        raise ValueError("No existe una entidad con ese ID.")

      model.nombre = producto.nombre
      model.descripcion = producto.descripcion
      model.precio_valor = producto.precio.valor
      model.precio_fecha = producto.precio.fecha
      model.moneda_id = producto.precio.moneda.id
      model.categoria_id = producto.categoria.id
      model.proveedor_id = producto.proveedor.id

    return producto

  def eliminar(self, id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(ProductoModel, id)

      if model is None:
        return False

      session.delete(model)
      return True


class RepositorioStock:
  """Repositorio SQLAlchemy para stock."""

  def crear(self, stock: Stock) -> Stock:
    with obtener_sesion() as session:
      model = StockModel(
        producto_id=stock.producto.id,
        cantidad=stock.cantidad,
      )
      session.add(model)
    return stock

  def leer_por_producto(self, producto_id: int) -> Optional[Stock]:
    with obtener_sesion() as session:
      stock = session.get(StockModel, producto_id)

      if stock is None:
        return None

      producto = session.get(ProductoModel, producto_id)

      producto_entidad = Producto(
        id=producto.id,
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=None,
        categoria=None,
        proveedor=None,
      )

      return Stock(
        producto=producto_entidad,
        cantidad=stock.cantidad,
      )

  def actualizar(self, stock: Stock) -> Stock:
    with obtener_sesion() as session:
      model = session.get(StockModel, stock.producto.id)

      if model is None:
        raise ValueError("No existe stock para ese producto.")

      model.cantidad = stock.cantidad

    return stock

  def eliminar(self, producto_id: int) -> bool:
    with obtener_sesion() as session:
      model = session.get(StockModel, producto_id)

      if model is None:
        return False

      session.delete(model)
      return True


class RepositorioCotizacionDolar:
  """Repositorio SQLAlchemy para cotizaciones del dólar."""

  def crear(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
    with obtener_sesion() as session:
      model = CotizacionDolarModel(
        valor=cotizacion.valor,
        fecha=cotizacion.fecha,
        tipo_id=cotizacion.tipo.id,
      )
      session.add(model)
    return cotizacion

  def leer_por_tipo_y_fecha(
    self,
    tipo_id: int,
    fecha: datetime.date,
  ) -> Optional[CotizacionDolar]:
    with obtener_sesion() as session:
      model = (
        session.query(CotizacionDolarModel)
        .filter(
          CotizacionDolarModel.tipo_id == tipo_id,
          CotizacionDolarModel.fecha == fecha,
        )
        .first()
      )

      if model is None:
        return None

      tipo = session.get(TipoCotizacionModel, model.tipo_id)

      return CotizacionDolar(
        valor=model.valor,
        fecha=model.fecha,
        tipo=TipoCotizacion(id=tipo.id, nombre=tipo.nombre),
      )

  def leer_historico_por_tipo(
    self,
    tipo_id: int,
  ) -> List[CotizacionDolar]:
    with obtener_sesion() as session:
      modelos = (
        session.query(CotizacionDolarModel)
        .filter(CotizacionDolarModel.tipo_id == tipo_id)
        .all()
      )

      tipo = session.get(TipoCotizacionModel, tipo_id)

      return [
        CotizacionDolar(
          valor=m.valor,
          fecha=m.fecha,
          tipo=TipoCotizacion(id=tipo.id, nombre=tipo.nombre),
        )
        for m in modelos
      ]

  def actualizar(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
    with obtener_sesion() as session:
      model = (
        session.query(CotizacionDolarModel)
        .filter(
          CotizacionDolarModel.tipo_id == cotizacion.tipo.id,
          CotizacionDolarModel.fecha == cotizacion.fecha,
        )
        .first()
      )

      if model is None:
        raise ValueError("No existe cotización para ese tipo y fecha.")

      model.valor = cotizacion.valor

    return cotizacion

  def eliminar(self, tipo_id: int, fecha: datetime.date) -> bool:
    with obtener_sesion() as session:
      model = (
        session.query(CotizacionDolarModel)
        .filter(
          CotizacionDolarModel.tipo_id == tipo_id,
          CotizacionDolarModel.fecha == fecha,
        )
        .first()
      )

      if model is None:
        return False

      session.delete(model)
      return True
