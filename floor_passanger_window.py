from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FloorPassengerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.show()


    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(511, 215)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.passenger_label = QLabel(Dialog)
        self.passenger_label.setObjectName(u"passenger_label")
        self.passenger_label.setWordWrap(True)

        self.gridLayout.addWidget(self.passenger_label, 0, 0, 1, 2)

        self.save_passenger_pb = QPushButton(Dialog)
        self.save_passenger_pb.setObjectName(u"save_passenger_pb")

        self.gridLayout.addWidget(self.save_passenger_pb, 2, 1, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.passenger_label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u0442\u0430\u0436 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430 1:", None))
        self.save_passenger_pb.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi