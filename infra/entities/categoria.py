from infra.configs.base import Base
from infra.entities.produto import Produto
from sqlalchemy import Column, String, Integer, ForeignKey


class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=True)

    def __repr__(self):
        return f'Nome da categoria = {self.nome_cat}, id = {self.id_cat}, id do Produto = {self.id_produto}'