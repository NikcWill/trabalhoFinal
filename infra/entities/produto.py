from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float, Boolean

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=True)
    preco = Column(Float, nullable=True)
    quantidade = Column(Integer, nullable=False)
    ativo = Column(Boolean, nullable=True)

    def __repr__(self):
        return f'Nome do produto = {self.nome}, id = {self.id}, preço = {self.preco}, quantidade = {self.quantidade}, ativo = {self.ativo}'