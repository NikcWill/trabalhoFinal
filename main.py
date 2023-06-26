from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Slot
from view.estoque import Ui_MainWindow

class TelaInicial(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_cadastrar.clicked.connect(self.abrir_segunda_tela)
        self.btn_saida_estoque_2.clicked.connect(self.voltar_tela_inicial)
        self.btn_salvar_2.clicked.connect(self.voltar_tela_inicial)
        self.tb_estoque.cellDoubleClicked.connect(self.abrir_segunda_tela)

    @Slot()
    def abrir_segunda_tela(self):
        self.tabWidget.setCurrentIndex(1)


    @Slot()
    def voltar_tela_inicial(self):
        self.tabWidget.setCurrentIndex(0)



if __name__ == '__main__':
    app = QApplication([])

    main_window = TelaInicial()
    main_window.show()

    app.exec()