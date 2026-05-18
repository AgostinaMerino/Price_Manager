import csv
import datetime
import os

from price_manager.database.connection import obtener_sesion

from price_manager.models.models import (
  CategoriaModel,
  CotizacionDolarModel,
  MonedaModel,
  ProductoModel,
  ProveedorModel,
  StockModel,
  TipoCotizacionModel,
)


def generar_insert_sql(
  tabla: str,
  columnas: list[str],
  valores: list,
) -> str:
  """Genera una sentencia INSERT SQL."""

  valores_sql = []

  for valor in valores:

    if isinstance(valor, str):
      valores_sql.append(f"'{valor}'")

    else:
      valores_sql.append(str(valor))

  columnas_sql = ", ".join(columnas)

  valores_sql = ", ".join(valores_sql)

  return (
    f"INSERT INTO {tabla} ({columnas_sql}) "
    f"VALUES ({valores_sql});"
  )


def guardar_sql(
  carpeta_sql: str,
  nombre_archivo: str,
  lineas_sql: list[str],
) -> None:
  """Guarda sentencias SQL en archivo."""

  os.makedirs(carpeta_sql, exist_ok=True)

  ruta = os.path.join(
    carpeta_sql,
    nombre_archivo,
  )

  with open(
    ruta,
    mode="w",
    encoding="utf-8",
  ) as archivo:

    archivo.write("\n".join(lineas_sql))


def migrar_datos(
  carpeta_csvs: str,
  carpeta_sqls: str,
) -> None:
  """Migra datos desde CSV hacia SQLite."""

  with obtener_sesion() as session:

    # =========================
    # Categorías
    # =========================

    sql_categoria = []

    ruta = os.path.join(
      carpeta_csvs,
      "categorias.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        categoria = CategoriaModel(
          id=int(fila["id"]),
          nombre=fila["nombre"],
        )

        session.add(categoria)

        sql_categoria.append(
          generar_insert_sql(
            "categorias",
            ["id", "nombre"],
            [
              fila["id"],
              fila["nombre"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "categorias.sql",
      sql_categoria,
    )

    # =========================
    # Proveedores
    # =========================

    sql_proveedores = []

    ruta = os.path.join(
      carpeta_csvs,
      "proveedores.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        proveedor = ProveedorModel(
          id=int(fila["id"]),
          nombre=fila["nombre"],
          contacto=fila["contacto"],
        )

        session.add(proveedor)

        sql_proveedores.append(
          generar_insert_sql(
            "proveedores",
            ["id", "nombre", "contacto"],
            [
              fila["id"],
              fila["nombre"],
              fila["contacto"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "proveedores.sql",
      sql_proveedores,
    )

    # =========================
    # Monedas
    # =========================

    sql_monedas = []

    ruta = os.path.join(
      carpeta_csvs,
      "monedas.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        moneda = MonedaModel(
          id=int(fila["id"]),
          nombre=fila["nombre"],
        )

        session.add(moneda)

        sql_monedas.append(
          generar_insert_sql(
            "monedas",
            ["id", "nombre"],
            [
              fila["id"],
              fila["nombre"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "monedas.sql",
      sql_monedas,
    )

    # =========================
    # Tipos cotización
    # =========================

    sql_tipos = []

    ruta = os.path.join(
      carpeta_csvs,
      "tipos_cotizacion.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        tipo = TipoCotizacionModel(
          id=int(fila["id"]),
          nombre=fila["nombre"],
        )

        session.add(tipo)

        sql_tipos.append(
          generar_insert_sql(
            "tipos_cotizacion",
            ["id", "nombre"],
            [
              fila["id"],
              fila["nombre"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "tipos_cotizacion.sql",
      sql_tipos,
    )

    # =========================
    # Productos
    # =========================

    sql_productos = []

    ruta = os.path.join(
      carpeta_csvs,
      "productos.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        producto = ProductoModel(
          id=int(fila["id"]),
          nombre=fila["nombre"],
          descripcion=fila["descripcion"],
          precio_valor=float(fila["precio_valor"]),
          precio_fecha=datetime.date.fromisoformat(
            fila["precio_fecha"]
          ),
          moneda_id=int(fila["moneda_id"]),
          categoria_id=int(fila["categoria_id"]),
          proveedor_id=int(fila["proveedor_id"]),
        )

        session.add(producto)

        sql_productos.append(
          generar_insert_sql(
            "productos",
            [
              "id",
              "nombre",
              "descripcion",
              "precio_valor",
              "precio_fecha",
              "moneda_id",
              "categoria_id",
              "proveedor_id",
            ],
            [
              fila["id"],
              fila["nombre"],
              fila["descripcion"],
              fila["precio_valor"],
              fila["precio_fecha"],
              fila["moneda_id"],
              fila["categoria_id"],
              fila["proveedor_id"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "productos.sql",
      sql_productos,
    )

    # =========================
    # Stock
    # =========================

    sql_stock = []

    ruta = os.path.join(
      carpeta_csvs,
      "stock.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        stock = StockModel(
          producto_id=int(fila["producto_id"]),
          cantidad=int(fila["cantidad"]),
        )

        session.add(stock)

        sql_stock.append(
          generar_insert_sql(
            "stocks",
            ["producto_id", "cantidad"],
            [
              fila["producto_id"],
              fila["cantidad"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "stocks.sql",
      sql_stock,
    )

    # =========================
    # Cotizaciones
    # =========================

    sql_cotizaciones = []

    ruta = os.path.join(
      carpeta_csvs,
      "cotizaciones.csv",
    )

    with open(
      ruta,
      mode="r",
      encoding="utf-8",
    ) as archivo:

      reader = csv.DictReader(archivo)

      for fila in reader:

        cotizacion = CotizacionDolarModel(
          valor=float(fila["valor"]),
          fecha=datetime.date.fromisoformat(
            fila["fecha"]
          ),
          tipo_id=int(fila["tipo_id"]),
        )

        session.add(cotizacion)

        sql_cotizaciones.append(
          generar_insert_sql(
            "cotizaciones_dolar",
            ["valor", "fecha", "tipo_id"],
            [
              fila["valor"],
              fila["fecha"],
              fila["tipo_id"],
            ],
          )
        )

    guardar_sql(
      carpeta_sqls,
      "cotizaciones_dolar.sql",
      sql_cotizaciones,
    )

  print("Migración finalizada correctamente.")
