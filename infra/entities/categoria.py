from infra.configs.base import Base
from sqlalchemy import Column, String, Integer


class Categoria(Base):
    __tablename__ = 'categoria'

    id_cat = Column(Integer, autoincrement=True, primary_key=True)
    nome_cat = Column(String(100), nullable=True)

    def __repr__(self):
         return f'Nome da categoria = {self.nome_cat}, id = {self.id_cat}'