from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
  "sqlite:////content/price_manager/price_manager.db"
)

engine = create_engine(
  DATABASE_URL,
  echo=False,
)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine,
)

Base = declarative_base()


class ConexionDB:
  """Administra la conexión a la base de datos."""

  def __init__(self) -> None:
    self.engine = engine

  def obtener_engine(self):
    """Devuelve el engine de SQLAlchemy."""
    return self.engine
