from infra.configs.connection import DBConnectionHandler
from infra.entities.produto import Produto


class ProdutoRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto).filter(Produto.id == id).first()
            return data

    def selectCat(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto).filter(Produto.id_categoria == id).all()
            return data

    def selectName(self, name):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto).filter(Produto.nome == name).all()
            return data

    def insert(self, produto):
        with DBConnectionHandler() as db:
            try:
                db.session.add(produto)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Produto).filter(Produto.id == id).delete()
            db.session.commit()

    def update(self, produto):
        with DBConnectionHandler() as db:

            try:
                db.session.query(Produto).filter(Produto.id == produto.id) \
                    .update({'nome': produto.nome, 'preco': produto.preco, 'quantidade': produto.quantidade, 'id_categoria': produto.id_categoria, 'ativo': produto.ativo})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e