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
                    .update({'titulo': produto.titulo, 'texto': produto.texto})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e