from infra.configs.connection import DBConnectionHandler
from infra.entities.categoria import Categoria


class CategoriaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Categoria).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Categoria).filter(Categoria.id_cat == id).first()
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
            db.session.query(Categoria).filter(Categoria.id_cat == id).delete()
            db.session.commit()

    def update(self, categoria):
        with DBConnectionHandler() as db:

            try:
                db.session.query(Categoria).filter(Categoria.id_cat == categoria.id_cat) \
                    .update({'nome_cat': categoria.nome_cat})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def insert_categorias(self):
        categorias_db = self.select_all()
        if len(categorias_db) == 0:
            categorias = [
                Categoria(nome_cat="Elétrica"),
                Categoria(nome_cat="Mecânica"),
                Categoria(nome_cat="Funilaria"),
                Categoria(nome_cat="Internos"),
            ]
            db = CategoriaRepository()

            for i in categorias:
                db.insert(i)