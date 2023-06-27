from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    id_categoria = Column(Integer, nullable=False)
    ativo = Column(String(20), nullable=False)

