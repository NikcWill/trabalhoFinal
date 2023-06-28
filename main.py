from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import Slot
from view.estoque import Ui_MainWindow
from view.tela_login import Ui_Login_tela

class TelaLogin(QMainWindow, Ui_Login_tela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.abrir_segunda_tela)

    def abrir_segunda_tela(self):
        self.hide()
        print("Abrindo tela de estoque")
        segunda_tela = TelaEstoque()
        segunda_tela.show()


class TelaEstoque(QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_cadastrar.clicked.connect(self.abrir_tela_produto)
        self.ui.btn_saida_estoque_2.clicked.connect(self.voltar_tela_estoque)
        self.ui.btn_salvar_2.clicked.connect(self.voltar_tela_estoque)
        self.ui.tb_estoque.cellDoubleClicked.connect(self.abrir_tela_produto)

    @Slot()
    def abrir_tela_produto(self):
        self.ui.tabWidget.setCurrentIndex(1)

    @Slot()
    def voltar_tela_estoque(self):
        self.ui.tabWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication([])

    main_window = TelaLogin()
    main_window.show()

    app.exec()
