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


from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session


@contextmanager
def obtener_sesion() -> Generator[Session, None, None]:
  """Administra sesiones transaccionales."""

  session = SessionLocal()

  try:
    yield session
    session.commit()

  except Exception:
    session.rollback()
    raise

  finally:
    session.close()
