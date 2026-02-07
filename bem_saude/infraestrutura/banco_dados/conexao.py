import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

from src.bem_saude.api.configuracoes import Configuracoes

logger = logging.getLogger(__name__)

#engine do sqlalchemy
#pool de conexões configurado para uso em prod.
#echo=false para não logar todas as queries no console

engine = create_engine(
    Configuracoes.DATABASE_URL,
    echo=False,
    pool_pre_ping=True, #Validar conexões antes de usá-las
    pool_size=5, # numero de conexões a serem mantidas no pool
    max_overflow=10, # conexoes extras que podem ser criadas além do pool_size
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def obter_sessao() -> Session:
    """
    Obtém uma sessão do banco de dados.

    Retorna uma sessão do banco de dados para interagir com o banco de dados.
    Garante que a sessão seja fechada após o uso.

    Yields:
        Session: Sessão do banco de dados.
    """
    db = SessionLocal()
    try:
        logger.debug("Sessão do banco de dados iniciada.")
        yield db
    finally:
        db.close()
        logger.debug("Sessão do banco de dados encerrada.")