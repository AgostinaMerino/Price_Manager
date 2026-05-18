from price_manager.migrations.migrations import migrar_datos
from price_manager.models.models import crear_tablas
from price_manager.preload_data.preload_data import precargar_datos
from price_manager.ui.console import main as ejecutar_menu


desactivar_git_push = False


def inicializar_base_datos() -> None:
  """Inicializa tablas y datos base."""

  crear_tablas()
  precargar_datos()

  migrar_datos(
    "/content/price_manager/src/price_manager/migrations/csv",
    "/content/price_manager/src/price_manager/migrations/sql",
  )


def main(import_default_data: bool = False) -> None:
  """Ejecuta el sistema."""

  if import_default_data:
    inicializar_base_datos()

  ejecutar_menu()


if __name__ == "__main__":
  main(import_default_data=True)
