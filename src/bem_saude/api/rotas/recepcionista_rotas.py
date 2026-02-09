from uuid import UUID
from fastapi import APIRouter, Depends, status
from bem_saude.api.schemas.recepcionista_schemas import RecepcionistaCriarRequest, RecepcionistaResponse


# Router para endpoint de recepcionistas
# Todas as rotas comeca com /recepcionistas


router = APIRouter(
    prefix="/recepcionistas",
    tags=["Recepcionista"]
)


@router.post(
    "", 
    response_model= RecepcionistaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo recepcionista",
    responses= {
        201: {
            "description": "Recepcionista criado com sucesso",
            "model": RecepcionistaResponse
        }
    }
)


def criar_recepcionista(dados: RecepcionistaCriarRequest) -> RecepcionistaResponse:
    return {"ok": "asokasd"}