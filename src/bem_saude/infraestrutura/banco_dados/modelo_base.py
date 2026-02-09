from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    """
    Classe base para todos os modelos ORM.
    """

    pass

class ModeloBase(Base):
    """
    Classe base para os modelos de dados, incluindo campos comuns.(criado_em, alterado_em)
    """

    __abstract__ = True

    criado_em = Column(DateTime, nullable=False, default=datetime.now)
    alterado_em = Column(DateTime, nullable=True, onupdate=datetime.now)
    