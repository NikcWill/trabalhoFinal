# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroProduto.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from infra.entities.produto import Produto
from infra.repository.produto_repository import ProdutoRepository
from infra.entities import *
from infra.configs import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 861)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.tela_estoque = QWidget()
        self.tela_estoque.setObjectName(u"tela_estoque")
        self.verticalLayout_5 = QVBoxLayout(self.tela_estoque)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.tela_estoque)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color:rgb(120, 120, 120)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_title = QLabel(self.frame)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_title)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.tela_estoque)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(120, 120, 120)")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_id = QLabel(self.frame_6)
        self.lbl_id.setObjectName(u"lbl_id")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.lbl_id.setFont(font1)

        self.verticalLayout_3.addWidget(self.lbl_id)

        self.txt_id = QLineEdit(self.frame_6)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_3.addWidget(self.txt_id)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_nome = QLabel(self.frame_9)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setFont(font1)

        self.verticalLayout_6.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.frame_9)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_6.addWidget(self.txt_nome)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_categoria = QLabel(self.frame_7)
        self.lbl_categoria.setObjectName(u"lbl_categoria")
        self.lbl_categoria.setFont(font1)

        self.verticalLayout_4.addWidget(self.lbl_categoria)

        self.txt_categoria = QLineEdit(self.frame_7)
        self.txt_categoria.setObjectName(u"txt_categoria")
        self.txt_categoria.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_4.addWidget(self.txt_categoria)


        self.verticalLayout_7.addWidget(self.frame_7)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.tela_estoque)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:rgb(120, 120, 120)")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_estoque = QTableWidget(self.frame_3)
        if (self.tb_estoque.columnCount() < 6):
            self.tb_estoque.setColumnCount(6)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        __qtablewidgetitem1.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        __qtablewidgetitem2.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        __qtablewidgetitem4.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        __qtablewidgetitem5.setBackground(QColor(231, 231, 231, 231));
        self.tb_estoque.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_estoque.setObjectName(u"tb_estoque")
        self.tb_estoque.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.tb_estoque.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.tb_estoque)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.tela_estoque)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setStyleSheet(u"background-color:rgb(160, 160, 160)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cadastrar = QPushButton(self.frame_5)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_cadastrar)

        self.btn_filtrar = QPushButton(self.frame_5)
        self.btn_filtrar.setObjectName(u"btn_filtrar")
        self.btn_filtrar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_filtrar)

        self.bt_limpar = QPushButton(self.frame_5)
        self.bt_limpar.setObjectName(u"bt_limpar")
        self.bt_limpar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.bt_limpar)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tela_estoque, "")
        self.tela_produto = QWidget()
        self.tela_produto.setObjectName(u"tela_produto")
        self.verticalLayout_14 = QVBoxLayout(self.tela_produto)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_8 = QFrame(self.tela_produto)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setStyleSheet(u"background-color:rgb(120, 120, 120)")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_title_2 = QLabel(self.frame_8)
        self.lbl_title_2.setObjectName(u"lbl_title_2")
        self.lbl_title_2.setFont(font)
        self.lbl_title_2.setStyleSheet(u"")
        self.lbl_title_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_title_2)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.tela_produto)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color:rgb(120, 120, 120)")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lbl_id_2 = QLabel(self.frame_11)
        self.lbl_id_2.setObjectName(u"lbl_id_2")
        self.lbl_id_2.setFont(font1)

        self.verticalLayout_11.addWidget(self.lbl_id_2)

        self.txt_id_2 = QLineEdit(self.frame_11)
        self.txt_id_2.setObjectName(u"txt_id_2")
        self.txt_id_2.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_11.addWidget(self.txt_id_2)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lbl_nome_2 = QLabel(self.frame_12)
        self.lbl_nome_2.setObjectName(u"lbl_nome_2")
        self.lbl_nome_2.setFont(font1)

        self.verticalLayout_12.addWidget(self.lbl_nome_2)

        self.txt_nome_2 = QLineEdit(self.frame_12)
        self.txt_nome_2.setObjectName(u"txt_nome_2")
        self.txt_nome_2.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_12.addWidget(self.txt_nome_2)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.widget_2 = QWidget(self.frame_10)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_preco_2 = QLabel(self.widget_2)
        self.lbl_preco_2.setObjectName(u"lbl_preco_2")
        self.lbl_preco_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.lbl_preco_2)

        self.txt_preco_2 = QLineEdit(self.widget_2)
        self.txt_preco_2.setObjectName(u"txt_preco_2")
        self.txt_preco_2.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_8.addWidget(self.txt_preco_2)


        self.verticalLayout_16.addWidget(self.widget_2)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lbl_quantidade_2 = QLabel(self.frame_13)
        self.lbl_quantidade_2.setObjectName(u"lbl_quantidade_2")
        self.lbl_quantidade_2.setFont(font1)

        self.verticalLayout_13.addWidget(self.lbl_quantidade_2)

        self.txt_quantidade_2 = QLineEdit(self.frame_13)
        self.txt_quantidade_2.setObjectName(u"txt_quantidade_2")
        self.txt_quantidade_2.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_13.addWidget(self.txt_quantidade_2)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.widget_3 = QWidget(self.frame_10)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lbl_categoria_2 = QLabel(self.widget_3)
        self.lbl_categoria_2.setObjectName(u"lbl_categoria_2")
        self.lbl_categoria_2.setFont(font1)

        self.verticalLayout_10.addWidget(self.lbl_categoria_2)

        self._2 = QHBoxLayout()
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.cb_1 = QCheckBox(self.widget_3)
        self.cb_1.setObjectName(u"cb_1")
        self.cb_1.setFont(font1)
        self.cb_1.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self._2.addWidget(self.cb_1)

        self.cb_2 = QCheckBox(self.widget_3)
        self.cb_2.setObjectName(u"cb_2")
        self.cb_2.setFont(font1)
        self.cb_2.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self._2.addWidget(self.cb_2)

        self.cb_3 = QCheckBox(self.widget_3)
        self.cb_3.setObjectName(u"cb_3")
        self.cb_3.setFont(font1)
        self.cb_3.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self._2.addWidget(self.cb_3)

        self.cb_4 = QCheckBox(self.widget_3)
        self.cb_4.setObjectName(u"cb_4")
        self.cb_4.setFont(font1)
        self.cb_4.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self._2.addWidget(self.cb_4)


        self.verticalLayout_10.addLayout(self._2)


        self.verticalLayout_16.addWidget(self.widget_3)

        self.widget = QWidget(self.frame_10)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.verticalLayout_15 = QVBoxLayout(self.widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lbl_ativo_2 = QLabel(self.widget)
        self.lbl_ativo_2.setObjectName(u"lbl_ativo_2")
        self.lbl_ativo_2.setFont(font1)

        self.verticalLayout_15.addWidget(self.lbl_ativo_2)

        self.cb_ativo = QComboBox(self.widget)
        self.cb_ativo.addItem("")
        self.cb_ativo.addItem("")
        self.cb_ativo.addItem("")
        self.cb_ativo.setObjectName(u"cb_ativo")
        self.cb_ativo.setFont(font1)
        self.cb_ativo.setStyleSheet(u"background-color:rgb(231, 231, 231)")

        self.verticalLayout_15.addWidget(self.cb_ativo)


        self.verticalLayout_16.addWidget(self.widget)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_14 = QFrame(self.tela_produto)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 100))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(500, 16777215))
        self.frame_15.setStyleSheet(u"background-color:rgb(160, 160, 160)")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_salvar_2 = QPushButton(self.frame_15)
        self.btn_salvar_2.setObjectName(u"btn_salvar_2")
        self.btn_salvar_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn_salvar_2)

        self.btn_limpar_2 = QPushButton(self.frame_15)
        self.btn_limpar_2.setObjectName(u"btn_limpar_2")
        self.btn_limpar_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn_limpar_2)

        self.btn_saida_estoque_2 = QPushButton(self.frame_15)
        self.btn_saida_estoque_2.setObjectName(u"btn_saida_estoque_2")
        self.btn_saida_estoque_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn_saida_estoque_2)


        self.horizontalLayout_3.addWidget(self.frame_15)


        self.verticalLayout_14.addWidget(self.frame_14)

        self.tabWidget.addTab(self.tela_produto, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE DE PRODUTOS", None))
        self.lbl_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.txt_id.setText("")
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_categoria.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        ___qtablewidgetitem = self.tb_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tb_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem3 = self.tb_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem4 = self.tb_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem5 = self.tb_estoque.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ativo", None));
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.bt_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_estoque), QCoreApplication.translate("MainWindow", u"tela_estoque", None))
        self.lbl_title_2.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.lbl_id_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.txt_id_2.setText("")
        self.lbl_nome_2.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_preco_2.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.lbl_quantidade_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.lbl_categoria_2.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.cb_1.setText(QCoreApplication.translate("MainWindow", u"El\u00e9trica", None))
        self.cb_2.setText(QCoreApplication.translate("MainWindow", u"Mec\u00e2nica", None))
        self.cb_3.setText(QCoreApplication.translate("MainWindow", u"Funilaria", None))
        self.cb_4.setText(QCoreApplication.translate("MainWindow", u"Internos", None))
        self.lbl_ativo_2.setText(QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.cb_ativo.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.cb_ativo.setItemText(1, QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.cb_ativo.setItemText(2, QCoreApplication.translate("MainWindow", u"Inativo", None))

        self.btn_salvar_2.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_limpar_2.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.btn_saida_estoque_2.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda de estoque", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela_produto), QCoreApplication.translate("MainWindow", u"tela_produto", None))

# Aqui comeã a lógica (chora moleque)

    def salvar_produto(self):

        db = ProdutoRepository()


        nota = Produto(

            nome=self.txt_nome_2.text(),
            preco=self.txt_preco_2.text(),
            quantidade=self.txt_quantidade_2.text(),
            categoria=self._verificar_categorias(),
            ativo=self.cb_ativo.currentText(),
        )

        if self.btn_salvar_2.text() == 'Salvar':
            retorno = db.insert(produto)
            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro de Nota ')
                msg.setText('Cadastro realizado com sucesso')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao cadastrar ')
                msg.setText('Erro ao cadastrar verfique os dados inseridos')
                msg.exec()


        elif self.btn_salvar.text() == 'Atualizar':
            nota.id = int(self.txt_id.text())
            retorno = db.update(nota)

            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Nota Atualizada ')
                msg.setText('Nota atualizada com sucesso')
                msg.exec()
                self.popular_tabela_notas()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Atualizar ')
                msg.setText('Erro ao atualizar verfique os dados inseridos')
                msg.exec()

        self.popular_tabela_notas()
        self.limpar_conteudo()

    def _verificar_categorias(self):
        caterias_selecionadas = []
        categorias = [self.cb_1, self.cb_2, self.cb_3, self.cb_4]
        for categoria in categorias:
            if categoria == selecionado:
                caterias_selecionadas.append(categorias.index(categoria))
        return caterias_selecionadas
