import os
from sqlmodel import SQLModel, create_engine
import logging

# Configuração para ocultar logs detalhados do SQLAlchemy
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

# Definindo a URL do banco de dados. Podemos usar variáveis de ambiente para maior flexibilidade.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")  # Usa o SQLite como padrão

# Configuração do engine de conexão sem logs desnecessários
engine = create_engine(DATABASE_URL, echo=False)  # 'echo=False' para desativar os logs do SQLAlchemy

def init_db():
    """
    Inicializa o banco de dados criando as tabelas necessárias.
    Esse método deve ser chamado uma vez no início da execução.
    """
    SQLModel.metadata.create_all(engine)  # Cria as tabelas no banco de dados
