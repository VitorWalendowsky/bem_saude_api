"""
Ponto de entrada para o módulo bem_saude.

Este modulo é o entry point para a aplicação BEM Saúde, responsável por configurar e iniciar a aplicação FastAPI. Ele importa as configurações, define a função de criação da aplicação e instancia a aplicação para ser executada. Este módulo é essencial para garantir que a aplicação seja configurada corretamente e esteja pronta para receber requisições.

uso:
    uvicorn src.bem_saude.principal:app --reload
ou para produção:
    uvicorn src.bem_saude.principal:app --host  0.0.0.0 --port 8000
"""

from bem_saude.api.app import app

__all__ = ["app"]   