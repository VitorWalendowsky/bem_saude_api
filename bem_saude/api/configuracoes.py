"""
Modulos de configuracao de aplicação
carrega variaveis de ambiente usando pydantic settings
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuracoes(BaseSettings):
    """
    Configurações da aplicação, carregadas a partir de variáveis de ambiente.

    A classe Configuracoes utiliza o Pydantic para validar e carregar as configurações necessárias para a aplicação, como a URL do banco de dados. As variáveis de ambiente são definidas em um arquivo .env localizado na raiz do projeto.

    """
# configuração do banco de dados
#formato: postgres: postgresql+psycopg://usuario:senha@host:porta/nome_do_banco
    DATABASE_URL: str

# contrrole se o swagger sera habilitado e outros comportamentos relacionados ao ambiente
    AMBIENTE: str = "desenvolvimento"

# nivel dde loggine (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    model_config = SettingsConfigDict(
        env_file = Path(__file__).parent.parent.parent / '.env',
        env_file_encoding = 'utf-8',
        case_sensitive = False
    )

    @property
    def is_producao(self) -> bool:
        return self.AMBIENTE.lower() == "producao"
    
    @property
    def swagger_habilitado(self) -> bool:
        return not self.is_producao
    
    configuracoes = Configuracoes()