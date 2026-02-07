"""
    Modelo ORM parra tabela de recepcionistas

    Mapeia a entidade Recepcionista para a tabela correspondente no banco de dados, incluindo campos como id, nome, email e telefone.
"""

from sqlalchemy import Column, Integer, String
from bem_saude.infraestrutura.banco_dados.modelo_base import ModeloBase
from sqlalchemy.dialects.postgresql import UUID


class ModeloRecepcionista(ModeloBase):
    """
    Modelo ORM para a tabela de recepcionistas.

    Mapeia os campos da entidade de dominio Recepcionista para as colunas da tabela no banco de dados.

    """

    __tablename__ = 'recepcionistas'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    nome = Column(String(45), nullable=False)
    status = Column(String(10), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telefone = Column(String(20), nullable=True)
