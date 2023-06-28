from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import Slot
from view.estoque import Ui_MainWindow
from view.tela_login import Ui_Login_tela
class TelaLogin(QMainWindow, Ui_Login_tela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(TelaInicial)

class TelaInicial(QMainWindow, Ui_MainWindow, Ui_Login_tela ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_cadastrar.clicked.connect(self.abrir_segunda_tela)
        self.btn_saida_estoque_2.clicked.connect(self.voltar_tela_inicial)
        self.btn_salvar_2.clicked.connect(self.voltar_tela_inicial)
        self.tb_estoque.cellDoubleClicked.connect(self.abrir_segunda_tela)


    def abrir_tela_login(self):
        self.tabWidget.show()
    @Slot()
    def abrir_segunda_tela(self):
        self.tabWidget.setCurrentIndex(1)


    @Slot()
    def voltar_tela_inicial(self):
        self.tabWidget.setCurrentIndex(0)



if __name__ == '__main__':
    app = QApplication([])
    tela_login = TelaInicial()
    tela_login.show()
    app.exec()