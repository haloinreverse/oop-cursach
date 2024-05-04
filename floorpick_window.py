from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FloorPickWindow(QDialog):
    lift_called_signal = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.call_lift_pb.clicked.connect(self.call_lift_pb_clicked)
        # self.show()

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 299)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.floor_number_label = QLabel(Dialog)
        self.floor_number_label.setObjectName(u"floor_number_label")

        self.verticalLayout.addWidget(self.floor_number_label)

        self.floor_number_le = QLineEdit(Dialog)
        self.floor_number_le.setObjectName(u"floor_number_le")

        self.verticalLayout.addWidget(self.floor_number_le)

        self.go_up_rb = QRadioButton(Dialog)
        self.go_up_rb.setObjectName(u"go_up_rb")

        self.go_up_rb.setChecked(True)

        self.verticalLayout.addWidget(self.go_up_rb)

        self.go_down_rb = QRadioButton(Dialog)
        self.go_down_rb.setObjectName(u"go_down_rb")

        self.verticalLayout.addWidget(self.go_down_rb)

        self.call_lift_pb = QPushButton(Dialog)
        self.call_lift_pb.setObjectName(u"call_lift_pb")

        self.verticalLayout.addWidget(self.call_lift_pb)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.floor_number_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u044d\u0442\u0430\u0436\u0430:", None))
        self.go_up_rb.setText(QCoreApplication.translate("Dialog", u"\u0415\u0445\u0430\u0442\u044c \u0432\u0432\u0435\u0440\u0445", None))
        self.go_down_rb.setText(QCoreApplication.translate("Dialog", u"\u0415\u0445\u0430\u0442\u044c \u0432\u043d\u0438\u0437", None))
        self.call_lift_pb.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c", None))
    # retranslateUi

    def call_lift_pb_clicked(self):
        floor = int(self.floor_number_le.text())
        self.close()
        direction = 0
        if self.go_up_rb.isChecked():
            direction = 1
        else:
            direction = -1
        self.lift_called_signal.emit((floor, direction))
