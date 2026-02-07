"""
Aplicação FastAPI para o projeto BEM Saúde.

Configura e inicializa a aplicação FastAPI, incluindo o registro de rotas, configuração de middlewares e integração com o banco de dados. A aplicação é estruturada para ser modular e escalável, permitindo fácil manutenção e adição de novas funcionalidades no futuro.
middlewares
tratadores de exceção
rotas
swagger

"""

import logging
from fastapi import FastAPI, logger
from bem_saude.api.configuracoes import Configuracoes

#configurar logging antes de crias a aplicação

logging.basicConfig(
    level=Configuracoes.LOG_LEVEL,
    format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def criar_aplicacao() -> FastAPI:
    if Configuracoes.is_producao:
        logger.info("Iniciando aplicação em modo produção. Swagger desabilitado.")
        app = FastAPI(
            docs_url=None,  # Desabilita /docs
            redoc_url=None,  # Desabilita /redoc
            openapi_url=None,  # Desabilita /openapi.json
        )
    else:
        logger.info("Iniciando aplicação em modo desenvolvimento. Swagger habilitado.")
        app = FastAPI(
            title="BEM Saúde API",
            version="1.0.0",
            docs_url="/docs",
            redoc_url="/redoc",
            openapi_url="/openapi.json"
        )
    
    logger.info("configurando middlewares de logs")

    logger.info("configurando tratadores de excessão")

    logger.info("registrando rotas")

    @app.get("/health", tags=["Saúde"], summary="heakth check", description="Verificar se API está respoondendo.")
    def health_check():
        return {
            "status": "ok",
            "ambiente": Configuracoes.AMBIENTE,
            "swagger_habilitado": Configuracoes.swagger_habilitado
        }

    logger.info("Aplicação criada com sucesso.")
    return app

#criar instancia da aplicação
app = criar_aplicacao()