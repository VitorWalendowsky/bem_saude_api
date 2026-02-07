"""
    Schemas pydantic para recepcionistas

    define os DTOs (data transfer objects para requisições e respostas relacionadas) a recepcionistas
"""

from datetime import datetime
from uuid import UUID  
from pydantic import BaseModel, EmailStr, Field
from bem_saude.dominio.enums.status_cadastro import StatusCadastro

class RecepcionistaCriarRequest(BaseModel):
    """
    Schema para criar um novo recepcionista.

    Define os campos necessários para criar um recepcionista, incluindo nome, email, telefone e status.
    """

nome: str = Field(
    ...,
    min_length=3,
    max_length=255,
    description="Nome completo do recepcionista",
    examples=["Mario dos Santos"]
)

status: StatusCadastro = Field(
    default=StatusCadastro.ATIVO,
    description="Status do cadastro",
    examples=["ATIVO"]
)

model_config = {
    "json_schema_extra": {
        "examples": {
            "nome": "Mario dos Santos",
            "status": "ATIVO"
        }
    }
}