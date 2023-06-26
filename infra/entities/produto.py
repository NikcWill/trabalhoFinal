from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=True)
    preco = Column(Float, nullable=True)
    quantidade = Column(Integer, nullable=False)
    id_categoria = Column(Integer, nullable=True)
    ativo = Column(String(20), nullable=True)

    def __repr__(self):
        return f'Nome do produto = {self.nome}, id = {self.id}, preço = {self.preco}, quantidade = {self.quantidade},id_categoria = {self.id_categoria} ativo = {self.ativo}'