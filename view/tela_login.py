# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QDir)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QHBoxLayout, QHeaderView, QLabel, QLayout,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget, QMessageBox, QInputDialog, QMenuBar, QStatusBar)

from infra.entities.produto import Produto
from infra.repository.produto_repository import ProdutoRepository
from infra.entities.categoria import Categoria
from infra.repository.categoria_repository import CategoriaRepository

# from tela import logo

class Ui_Login_tela(object):
    def setupUi(self, Login_tela):
        if not Login_tela.objectName():
            Login_tela.setObjectName(u"Login_tela")
        Login_tela.resize(899, 844)
        Login_tela.setStyleSheet(u"background-color:rgb(0,139,139)")
        self.centralwidget = QWidget(Login_tela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(11, 11, 877, 241))
        self.frame_4.setStyleSheet(u"background-color:rgb(0,139,139)")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_logo = QLabel(self.frame_4)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(40, 10, 801, 211))
        self.label_logo.setPixmap(QPixmap(u":/logo/Sem t\u00edtulo.png"))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(11, 259, 881, 531))
        self.frame_3.setStyleSheet(u"background-color:rgb(0,139,139)")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:rgb(95,158,160)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_login = QLabel(self.frame_6)
        self.lbl_login.setObjectName(u"lbl_login")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lbl_login.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_login)

        self.txt_login = QLineEdit(self.frame_6)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setStyleSheet(u"background-color:rgb(255, 255, 255);border-radius: 4px;")

        self.verticalLayout_3.addWidget(self.txt_login)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color:rgb(95,158,160)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_senha = QLabel(self.frame_9)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setFont(font)

        self.verticalLayout_6.addWidget(self.lbl_senha)

        self.txt_senha = QLineEdit(self.frame_9)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"background-color:rgb(255, 255, 255);border-radius: 4px;")

        self.verticalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color:rgb(95,158,160)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color:rgb(255, 255, 255);border-radius: 4px;")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.frame_7)

        Login_tela.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login_tela)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 899, 26))
        Login_tela.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login_tela)
        self.statusbar.setObjectName(u"statusbar")
        Login_tela.setStatusBar(self.statusbar)

        self.retranslateUi(Login_tela)

        QMetaObject.connectSlotsByName(Login_tela)
    # setupUi

    def retranslateUi(self, Login_tela):
        Login_tela.setWindowTitle(QCoreApplication.translate("Login_tela", u"MainWindow", None))
        self.label_logo.setText("")
        self.lbl_login.setText(QCoreApplication.translate("Login_tela", u"LOGIN", None))
        self.txt_login.setText("")
        self.lbl_senha.setText(QCoreApplication.translate("Login_tela", u"SENHA", None))
        self.pushButton.setText(QCoreApplication.translate("Login_tela", u"ENTRAR", None))
        # self.pushButton.clicked.connect(self)
    # retranslateUi

