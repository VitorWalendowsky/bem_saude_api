# Router para endpoints de recepcionistas
# Todas as rotas começam com /recepcionistas

from fastapi import APIRouter, Depends, status

from src.bem_saude.api.schemas.recepcionista_schemas import RecepcionistaCriarRequest

from uuid import UUID



router = APIRouter(
    prefix="/recepcionistas",
    tags=["Recepcionista"]
)

@router.post(
    "",
    response_model=RecepcionistaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo recepcionista",
    responses={
        201: {
            "description": "Recepcionista criado com sucesso",
            "model": RecepcionistaResponse
        }
    }
)

def criar_recepcionista(request: RecepcionistaCriarRequest):