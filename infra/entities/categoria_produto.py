from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, PrimaryKeyConstraint
from infra.entities import produto, categoria


class CategoriaProduto(Base):
    __tablename__ = 'categoria_produto'
    __table_args__ = (
        PrimaryKeyConstraint('produto_id', 'categoria_id'),
    )

    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)

    def __repr__(self):
        return f'Nome do produto = {self.nome}, id = {self.id}, preço = {self.preco}, quantidade = {self.quantidade}, ativo = {self.ativo}'
