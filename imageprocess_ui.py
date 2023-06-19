# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageProcess.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_upload_img = QPushButton(self.centralwidget)
        self.button_upload_img.setObjectName(u"button_upload_img")
        self.button_upload_img.setGeometry(QRect(20, 620, 100, 41))
        self.label_img_path = QLabel(self.centralwidget)
        self.label_img_path.setObjectName(u"label_img_path")
        self.label_img_path.setGeometry(QRect(20, 720, 81, 31))
        self.view_img_path = QLabel(self.centralwidget)
        self.view_img_path.setObjectName(u"view_img_path")
        self.view_img_path.setGeometry(QRect(100, 720, 491, 31))
        self.view_image_ploygon = QGraphicsView(self.centralwidget)
        self.view_image_ploygon.setObjectName(u"view_image_ploygon")
        self.view_image_ploygon.setGeometry(QRect(10, 30, 581, 571))
        self.list_clicked_points = QListWidget(self.centralwidget)
        self.list_clicked_points.setObjectName(u"list_clicked_points")
        self.list_clicked_points.setGeometry(QRect(610, 30, 261, 341))
        self.button_predict = QPushButton(self.centralwidget)
        self.button_predict.setObjectName(u"button_predict")
        self.button_predict.setGeometry(QRect(20, 670, 100, 41))
        self.show_oroginal_img = QLabel(self.centralwidget)
        self.show_oroginal_img.setObjectName(u"show_oroginal_img")
        self.show_oroginal_img.setGeometry(QRect(20, 10, 101, 16))
        self.show_clicked_points = QLabel(self.centralwidget)
        self.show_clicked_points.setObjectName(u"show_clicked_points")
        self.show_clicked_points.setGeometry(QRect(620, 10, 101, 16))
        self.list_detected_objects = QListWidget(self.centralwidget)
        self.list_detected_objects.setObjectName(u"list_detected_objects")
        self.list_detected_objects.setGeometry(QRect(610, 410, 261, 341))
        self.show_detected_objects = QLabel(self.centralwidget)
        self.show_detected_objects.setObjectName(u"show_detected_objects")
        self.show_detected_objects.setGeometry(QRect(620, 390, 111, 16))
        self.button_clear_lists = QPushButton(self.centralwidget)
        self.button_clear_lists.setObjectName(u"button_clear_lists")
        self.button_clear_lists.setGeometry(QRect(130, 620, 100, 41))
        self.slider_polygon_opacity = QSlider(self.centralwidget)
        self.slider_polygon_opacity.setObjectName(u"slider_polygon_opacity")
        self.slider_polygon_opacity.setGeometry(QRect(249, 630, 221, 25))
        self.slider_polygon_opacity.setOrientation(Qt.Horizontal)
        self.radioButton_points_lines_opacity = QRadioButton(self.centralwidget)
        self.radioButton_points_lines_opacity.setObjectName(u"radioButton_points_lines_opacity")
        self.radioButton_points_lines_opacity.setGeometry(QRect(250, 670, 221, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_upload_img.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.label_img_path.setText(QCoreApplication.translate("MainWindow", u"Image Path:", None))
        self.view_img_path.setText("")
        self.button_predict.setText(QCoreApplication.translate("MainWindow", u"Start Predict", None))
        self.show_oroginal_img.setText(QCoreApplication.translate("MainWindow", u"Original Image:", None))
        self.show_clicked_points.setText(QCoreApplication.translate("MainWindow", u"Click Points:", None))
        self.show_detected_objects.setText(QCoreApplication.translate("MainWindow", u"Detected Objects:", None))
        self.button_clear_lists.setText(QCoreApplication.translate("MainWindow", u"Clear Lists", None))
        self.radioButton_points_lines_opacity.setText(QCoreApplication.translate("MainWindow", u"Points and Lines Opacity", None))
    # retranslateUi

