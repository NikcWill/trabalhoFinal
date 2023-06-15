from infra.configs.connection import DBConnectionHandler
from infra.entities.categoria import Categoria


class CategoriaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Categoria).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Categoria).filter(Categoria.id == id).first()
            return data

    def insert(self, categoria):
        with DBConnectionHandler() as db:
            try:
                db.session.add(categoria)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Categoria).filter(Categoria.id == id).delete()
            db.session.commit()

    def update(self, categoria):
        with DBConnectionHandler() as db:

            try:
                db.session.query(Categoria).filter(Categoria.id == categoria.id) \
                    .update({'titulo': categoria.titulo, 'texto': categoria.texto})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e