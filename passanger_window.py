from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PassangerWindow(QDialog):
    save_passenger_signal = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.save_passenger_pb.clicked.connect(self.save_passenger_pb_clicked)
        # self.show()

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(483, 433)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.floornum8_label = QLabel(Dialog)
        self.floornum8_label.setObjectName(u"floornum8_label")

        self.gridLayout.addWidget(self.floornum8_label, 2, 0, 1, 1)

        self.up_le_2 = QLineEdit(Dialog)
        self.up_le_2.setObjectName(u"up_le_2")

        self.gridLayout.addWidget(self.up_le_2, 8, 2, 1, 1)

        self.down_le_6 = QLineEdit(Dialog)
        self.down_le_6.setObjectName(u"down_le_6")

        self.gridLayout.addWidget(self.down_le_6, 4, 4, 1, 1)

        self.floornum6_label = QLabel(Dialog)
        self.floornum6_label.setObjectName(u"floornum6_label")

        self.gridLayout.addWidget(self.floornum6_label, 4, 0, 1, 1)

        self.up_le_5 = QLineEdit(Dialog)
        self.up_le_5.setObjectName(u"up_le_5")

        self.gridLayout.addWidget(self.up_le_5, 5, 2, 1, 1)

        self.down_le_2 = QLineEdit(Dialog)
        self.down_le_2.setObjectName(u"down_le_2")

        self.gridLayout.addWidget(self.down_le_2, 8, 4, 1, 1)

        self.floornum1_label = QLabel(Dialog)
        self.floornum1_label.setObjectName(u"floornum1_label")

        self.gridLayout.addWidget(self.floornum1_label, 9, 0, 1, 1)

        self.down_le_7 = QLineEdit(Dialog)
        self.down_le_7.setObjectName(u"down_le_7")

        self.gridLayout.addWidget(self.down_le_7, 3, 4, 1, 1)

        self.up_label_5 = QLabel(Dialog)
        self.up_label_5.setObjectName(u"up_label_5")

        self.gridLayout.addWidget(self.up_label_5, 5, 1, 1, 1)

        self.up_label_3 = QLabel(Dialog)
        self.up_label_3.setObjectName(u"up_label_3")

        self.gridLayout.addWidget(self.up_label_3, 7, 1, 1, 1)

        self.up_label_8 = QLabel(Dialog)
        self.up_label_8.setObjectName(u"up_label_8")

        self.gridLayout.addWidget(self.up_label_8, 2, 1, 1, 1)

        self.down_label_5 = QLabel(Dialog)
        self.down_label_5.setObjectName(u"down_label_5")

        self.gridLayout.addWidget(self.down_label_5, 5, 3, 1, 1)

        self.floornum9_label = QLabel(Dialog)
        self.floornum9_label.setObjectName(u"floornum9_label")

        self.gridLayout.addWidget(self.floornum9_label, 1, 0, 1, 1)

        self.up_le_8 = QLineEdit(Dialog)
        self.up_le_8.setObjectName(u"up_le_8")

        self.gridLayout.addWidget(self.up_le_8, 2, 2, 1, 1)

        self.down_label_6 = QLabel(Dialog)
        self.down_label_6.setObjectName(u"down_label_6")

        self.gridLayout.addWidget(self.down_label_6, 4, 3, 1, 1)

        self.up_le_7 = QLineEdit(Dialog)
        self.up_le_7.setObjectName(u"up_le_7")

        self.gridLayout.addWidget(self.up_le_7, 3, 2, 1, 1)

        self.down_le_4 = QLineEdit(Dialog)
        self.down_le_4.setObjectName(u"down_le_4")

        self.gridLayout.addWidget(self.down_le_4, 6, 4, 1, 1)

        self.down_le_3 = QLineEdit(Dialog)
        self.down_le_3.setObjectName(u"down_le_3")

        self.gridLayout.addWidget(self.down_le_3, 7, 4, 1, 1)

        self.up_label_6 = QLabel(Dialog)
        self.up_label_6.setObjectName(u"up_label_6")

        self.gridLayout.addWidget(self.up_label_6, 4, 1, 1, 1)

        self.down_le_8 = QLineEdit(Dialog)
        self.down_le_8.setObjectName(u"down_le_8")

        self.gridLayout.addWidget(self.down_le_8, 2, 4, 1, 1)

        self.up_le_4 = QLineEdit(Dialog)
        self.up_le_4.setObjectName(u"up_le_4")

        self.gridLayout.addWidget(self.up_le_4, 6, 2, 1, 1)

        self.down_label_8 = QLabel(Dialog)
        self.down_label_8.setObjectName(u"down_label_8")

        self.gridLayout.addWidget(self.down_label_8, 2, 3, 1, 1)

        self.up_label_7 = QLabel(Dialog)
        self.up_label_7.setObjectName(u"up_label_7")

        self.gridLayout.addWidget(self.up_label_7, 3, 1, 1, 1)

        self.down_le_5 = QLineEdit(Dialog)
        self.down_le_5.setObjectName(u"down_le_5")

        self.gridLayout.addWidget(self.down_le_5, 5, 4, 1, 1)

        self.down_label_4 = QLabel(Dialog)
        self.down_label_4.setObjectName(u"down_label_4")

        self.gridLayout.addWidget(self.down_label_4, 6, 3, 1, 1)

        self.floornum4_label = QLabel(Dialog)
        self.floornum4_label.setObjectName(u"floornum4_label")

        self.gridLayout.addWidget(self.floornum4_label, 6, 0, 1, 1)

        self.liftname_label = QLabel(Dialog)
        self.liftname_label.setObjectName(u"liftname_label")

        self.gridLayout.addWidget(self.liftname_label, 0, 2, 1, 1)

        self.floornum5_label = QLabel(Dialog)
        self.floornum5_label.setObjectName(u"floornum5_label")

        self.gridLayout.addWidget(self.floornum5_label, 5, 0, 1, 1)

        self.down_label_2 = QLabel(Dialog)
        self.down_label_2.setObjectName(u"down_label_2")

        self.gridLayout.addWidget(self.down_label_2, 8, 3, 1, 1)

        self.up_le_3 = QLineEdit(Dialog)
        self.up_le_3.setObjectName(u"up_le_3")

        self.gridLayout.addWidget(self.up_le_3, 7, 2, 1, 1)

        self.floornum2_label = QLabel(Dialog)
        self.floornum2_label.setObjectName(u"floornum2_label")

        self.gridLayout.addWidget(self.floornum2_label, 8, 0, 1, 1)

        self.up_label_2 = QLabel(Dialog)
        self.up_label_2.setObjectName(u"up_label_2")

        self.gridLayout.addWidget(self.up_label_2, 8, 1, 1, 1)

        self.up_le_6 = QLineEdit(Dialog)
        self.up_le_6.setObjectName(u"up_le_6")

        self.gridLayout.addWidget(self.up_le_6, 4, 2, 1, 1)

        self.up_label_4 = QLabel(Dialog)
        self.up_label_4.setObjectName(u"up_label_4")

        self.gridLayout.addWidget(self.up_label_4, 6, 1, 1, 1)

        self.down_label_9 = QLabel(Dialog)
        self.down_label_9.setObjectName(u"down_label_9")

        self.gridLayout.addWidget(self.down_label_9, 1, 3, 1, 1)

        self.floornum3_label = QLabel(Dialog)
        self.floornum3_label.setObjectName(u"floornum3_label")

        self.gridLayout.addWidget(self.floornum3_label, 7, 0, 1, 1)

        self.floornum7_label = QLabel(Dialog)
        self.floornum7_label.setObjectName(u"floornum7_label")

        self.gridLayout.addWidget(self.floornum7_label, 3, 0, 1, 1)

        self.up_label_1 = QLabel(Dialog)
        self.up_label_1.setObjectName(u"up_label_1")

        self.gridLayout.addWidget(self.up_label_1, 9, 1, 1, 1)

        self.up_le_1 = QLineEdit(Dialog)
        self.up_le_1.setObjectName(u"up_le_1")

        self.gridLayout.addWidget(self.up_le_1, 9, 2, 1, 1)

        self.down_le_9 = QLineEdit(Dialog)
        self.down_le_9.setObjectName(u"down_le_9")

        self.gridLayout.addWidget(self.down_le_9, 1, 4, 1, 1)

        self.down_label_3 = QLabel(Dialog)
        self.down_label_3.setObjectName(u"down_label_3")

        self.gridLayout.addWidget(self.down_label_3, 7, 3, 1, 1)

        self.down_label_7 = QLabel(Dialog)
        self.down_label_7.setObjectName(u"down_label_7")

        self.gridLayout.addWidget(self.down_label_7, 3, 3, 1, 1)

        self.save_passenger_pb = QPushButton(Dialog)
        self.save_passenger_pb.setObjectName(u"save_passenger_pb")

        self.gridLayout.addWidget(self.save_passenger_pb, 10, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.floornum8_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 8", None))
        self.up_le_2.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_le_6.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.floornum6_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 6", None))
        self.up_le_5.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_le_2.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.floornum1_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 1", None))
        self.down_le_7.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.up_label_5.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.up_label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.up_label_8.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.down_label_5.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.floornum9_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 9", None))
        self.up_le_8.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_label_6.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.up_le_7.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_le_4.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_le_3.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.up_label_6.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.down_le_8.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.up_le_4.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_label_8.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.up_label_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.down_le_5.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.floornum4_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 4", None))
        self.liftname_label.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0444\u0442 \u043f\u043e\u0434\u044a\u0435\u0437\u0434\u0430 1", None))
        self.floornum5_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 5", None))
        self.down_label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.up_le_3.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.floornum2_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 2", None))
        self.up_label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.up_le_6.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.up_label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.down_label_9.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.floornum3_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 3", None))
        self.floornum7_label.setText(QCoreApplication.translate("Dialog", u"\u042d\u0442\u0430\u0436 7", None))
        self.up_label_1.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0440\u0445:", None))
        self.up_le_1.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_le_9.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.down_label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.down_label_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u043d\u0438\u0437:", None))
        self.save_passenger_pb.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

    def save_passenger_pb_clicked(self):
        passengers = []
        passengers.append((int(self.up_le_1.text()), 0))
        passengers.append((int(self.up_le_2.text()), int(self.down_le_2.text())))
        passengers.append((int(self.up_le_3.text()), int(self.down_le_3.text())))
        passengers.append((int(self.up_le_4.text()), int(self.down_le_4.text())))
        passengers.append((int(self.up_le_5.text()), int(self.down_le_5.text())))
        passengers.append((int(self.up_le_6.text()), int(self.down_le_6.text())))
        passengers.append((int(self.up_le_7.text()), int(self.down_le_7.text())))
        passengers.append((int(self.up_le_8.text()), int(self.down_le_8.text())))
        passengers.append((0, int(self.down_le_9.text())))

        self.save_passenger_signal.emit(passengers)
