from infra.configs.connection import DBConnectionHandler
from infra.entities import categoria
from infra.entities.categoria import Categoria
from infra.entities.produto import Produto


class ProdutoRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Produto, Categoria.nome_cat).join(Categoria,
                                                                  Produto.id_categoria == Categoria.id_cat).filter(
                Produto.id == id).first()

            if data is not None:
                produto, categoria.nome_cat = data
                produto.id_categoria = categoria.nome_cat
            return produto

    def select_name(self, nome):
        with DBConnectionHandler() as db:
            query = db.session.query(Produto).join(Categoria, Produto.id_categoria == Categoria.id_cat)
            query = query.filter(Produto.nome == nome)
            produtos = query.all()

            for produto in produtos:
                produto.id_categoria = Categoria.nome_cat

            return produtos

    # def select_name(self, nome):
    #     with DBConnectionHandler() as db:
    #         data = db.session.query(Produto, Categoria.nome_cat).join(Categoria,
    #                                                                   Produto.id_categoria == Categoria.id_cat).filter(
    #             Produto.nome == nome).first()
    #
    #         if data is not None:
    #             produto_name, categoria.nome_cat = data
    #             produto_name.id_categoria = categoria.nome_cat
    #         return produto_name

    def select_categoria(self, categoria):
        with DBConnectionHandler() as db:
            with DBConnectionHandler() as db:
                data = db.session.query(Produto, Categoria.nome_cat).join(Categoria,
                                                                          Produto.id_categoria == Categoria.id_cat).filter(
                    Produto.id_categoria == categoria.nome_cat).first()

                if data is not None:
                    produto_categoria, categoria.nome_cat = data
                    produto_categoria.id_categoria = categoria.nome_cat
                return produto_categoria

    # def select(self, id=None, nome=None, categoria=None):
    #     with DBConnectionHandler() as db:
    #         query = db.session.query(Produto)
    #
    #         if id is not None:
    #             query = query.join(Categoria, Produto.id_categoria == Categoria.id_cat)
    #             query = query.filter(Produto.id == id)
    #             query = query.with_entities(Produto, Categoria.nome_cat)
    #             produto = query.first()
    #
    #             if produto is not None:
    #                 produto, categoria_nome = produto
    #                 produto.id_categoria = categoria_nome
    #
    #             return produto
    #
    #         elif nome is not None:
    #             query = query.join(Categoria, Produto.id_categoria == Categoria.id_cat)
    #             query = query.filter(Produto.nome == nome)
    #             query = query.with_entities(Produto, Categoria.nome_cat)
    #             produto = query.first()
    #
    #             if produto is not None:
    #                 produto, categoria_nome = produto
    #                 produto.id_categoria = categoria_nome
    #
    #         if categoria is not None:
    #             query = query.filter(Produto.id_categoria == categoria)
    #             return query.first()
    #
    #         return query.all()

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