from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DisplayWindow(QMainWindow):
    def __init__(self):
        self.elevator1_floor = 0
        self.elevator2_floor = 0
        super().__init__()
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.elevator1_label = QLabel(self.centralwidget)
        self.elevator1_label.setObjectName(u"elevator1_label")

        self.gridLayout.addWidget(self.elevator1_label, 0, 0, 1, 1)

        self.elevator1_tw = QTableWidget(self.centralwidget)
        if (self.elevator1_tw.columnCount() < 2):
            self.elevator1_tw.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.elevator1_tw.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.elevator1_tw.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.elevator1_tw.rowCount() < 9):
            self.elevator1_tw.setRowCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.elevator1_tw.setVerticalHeaderItem(8, __qtablewidgetitem10)
        self.elevator1_tw.setObjectName(u"elevator1_tw")
        for i in range(2):
            for j in range(9):
                self.elevator1_tw.setItem(j, i, QTableWidgetItem())


        self.gridLayout.addWidget(self.elevator1_tw, 1, 0, 1, 1)

        self.elevator2_tw = QTableWidget(self.centralwidget)
        if (self.elevator2_tw.columnCount() < 2):
            self.elevator2_tw.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.elevator2_tw.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.elevator2_tw.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.elevator2_tw.rowCount() < 9):
            self.elevator2_tw.setRowCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.elevator2_tw.setVerticalHeaderItem(8, __qtablewidgetitem21)
        self.elevator2_tw.setObjectName(u"elevator2_tw")
        for i in range(2):
            for j in range(9):
                self.elevator2_tw.setItem(j, i, QTableWidgetItem())

        self.gridLayout.addWidget(self.elevator2_tw, 1, 1, 1, 1)

        self.elevator2_label = QLabel(self.centralwidget)
        self.elevator2_label.setObjectName(u"elevator2_label")

        self.gridLayout.addWidget(self.elevator2_label, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.elevator1_tw.item(8, 0).setBackground(QColor("green"))
        self.elevator2_tw.item(8, 0).setBackground(QColor("green"))
        self.elevator1_tw.item(8, 0).setText('0')
        self.elevator2_tw.item(8, 0).setText('0')
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.elevator1_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u044a\u0435\u0437\u0434 1", None))
        ___qtablewidgetitem = self.elevator1_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"elevator", None));
        ___qtablewidgetitem1 = self.elevator1_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Floor", None));
        ___qtablewidgetitem2 = self.elevator1_tw.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem3 = self.elevator1_tw.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem4 = self.elevator1_tw.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem5 = self.elevator1_tw.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem6 = self.elevator1_tw.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.elevator1_tw.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.elevator1_tw.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.elevator1_tw.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem10 = self.elevator1_tw.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.elevator2_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"elevator", None));
        ___qtablewidgetitem12 = self.elevator2_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Floor", None));
        ___qtablewidgetitem13 = self.elevator2_tw.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem14 = self.elevator2_tw.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem15 = self.elevator2_tw.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem16 = self.elevator2_tw.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem17 = self.elevator2_tw.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem18 = self.elevator2_tw.verticalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem19 = self.elevator2_tw.verticalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem20 = self.elevator2_tw.verticalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem21 = self.elevator2_tw.verticalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.elevator2_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u044a\u0435\u0437\u0434 2", None))
    # retranslateUi

    def set_passengers_elevator1(self, passengers, floor):
        i = self.elevator1_tw.item(0, 1)
        self.elevator1_tw.item(8 - floor, 1).setText(f'↑: {passengers[0]} ↓: {passengers[1]}')

    def change_passengers_elevator1(self, passengers, floor, direction):
        num_up = int(self.elevator1_tw.item(8 - floor, 1).text().split(' ↓: ')[0].split('↑: ')[1])
        num_down = int(self.elevator1_tw.item(8 - floor, 1).text().split('↓: ')[1])
        if direction == 1:
            self.elevator1_tw.item(8 - floor, 1).setText(f'↑: {num_up - passengers} ↓: {num_down}')
        else:
            self.elevator1_tw.item(8 - floor, 1).setText(f'↑: {num_up} ↓: {num_down - passengers}')

    def set_passengers_elevator2(self, passengers, floor):
        self.elevator2_tw.item(8 - floor, 1).setText(f'↑: {passengers[0]} ↓: {passengers[1]}')

    def change_passengers_elevator2(self, passengers, floor, direction):
        num_up = int(self.elevator2_tw.item(8 - floor, 1).text().split(' ↓: ')[0].split('↑: ')[1])
        num_down = int(self.elevator2_tw.item(8 - floor, 1).text().split('↓: ')[1])
        if direction == 1:
            self.elevator2_tw.item(8 - floor, 1).setText(f'↑: {num_up - passengers} ↓: {num_down}')
        else:
            self.elevator2_tw.item(8 - floor, 1).setText(f'↑: {num_up} ↓: {num_down - passengers}')


    def change_elevator_floor(self, num_elevator, new_floor):
        print('change elev flor')
        if num_elevator == 0:
            self.elevator1_tw.item(8 - self.elevator1_floor, 0).setBackground(QColor("white"))
            text = self.elevator1_tw.item(8 - self.elevator1_floor, 0).text()
            self.elevator1_tw.item(8 - self.elevator1_floor, 0).setText("")
            self.elevator1_floor = new_floor
            self.elevator1_tw.item(8 - self.elevator1_floor, 0).setBackground(QColor("green"))
            self.elevator1_tw.item(8 - self.elevator1_floor, 0).setText(text)
        else:
            self.elevator2_tw.item(8 - self.elevator2_floor, 0).setBackground(QColor("white"))
            text = self.elevator2_tw.item(8 - self.elevator2_floor, 0).text()
            self.elevator2_tw.item(8 - self.elevator2_floor, 0).setText("")
            self.elevator2_floor = new_floor
            self.elevator2_tw.item(8 - self.elevator2_floor, 0).setBackground(QColor("green"))
            self.elevator2_tw.item(8 - self.elevator2_floor, 0).setText(text)
        self.repaint()

    def change_elevator_num(self, num_elevator, change_num):
        if num_elevator == 0:
            new_num = int(self.elevator1_tw.item(8 - self.elevator1_floor, 0).text()) + change_num
            self.elevator1_tw.item(8 - self.elevator1_floor, 0).setText(str(new_num))
        else:
            new_num = int(self.elevator2_tw.item(8 - self.elevator2_floor, 0).text()) + change_num
            self.elevator2_tw.item(8 - self.elevator2_floor, 0).setText(str(new_num))
