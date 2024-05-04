from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from display_window import DisplayWindow
from main import House
from passanger_window import PassangerWindow
from floorpick_window import FloorPickWindow
from floor_passanger_window import FloorPassengerWindow

class ControlWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.house = House(2, 0, 0)

        self.display_window = DisplayWindow()
        self.display_window.show()

        self.passenger_window_1 = PassangerWindow()
        self.passenger_window_2 = PassangerWindow()
        self.passenger_window_2.liftname_label.setText('Лифт подъезда 2')
        self.lift1_passenger_bt.clicked.connect(self.lift1_passenger_bt_clicked)
        self.lift2_passenger_bt.clicked.connect(self.lift2_passenger_bt_clicked)
        self.passenger_window_1.save_passenger_signal.connect(self.lift1_save_all_passenger)
        self.passenger_window_2.save_passenger_signal.connect(self.lift2_save_all_passenger)



        self.floorpick_window_1 = FloorPickWindow()
        self.floorpick_window_2 = FloorPickWindow()
        self.lift1_floorpick_bt.clicked.connect(self.lift1_floorpick_bt_clicked)
        self.lift2_floorpick_bt.clicked.connect(self.lift2_floorpick_bt_clicked)
        self.floorpick_window_1.lift_called_signal.connect(self.lift1_called)
        self.floorpick_window_2.lift_called_signal.connect(self.lift2_called)




        # self.

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 303)
        self.lift1_floorpick_bt = QPushButton(Dialog)
        self.lift1_floorpick_bt.setObjectName(u"lift1_floorpick_bt")
        self.lift1_floorpick_bt.setGeometry(QRect(10, 110, 386, 32))
        self.lift1_passenger_bt = QPushButton(Dialog)
        self.lift1_passenger_bt.setObjectName(u"lift1_passenger_bt")
        self.lift1_passenger_bt.setGeometry(QRect(10, 60, 386, 32))
        self.lift2_passenger_bt = QPushButton(Dialog)
        self.lift2_passenger_bt.setObjectName(u"lift2_passenger_bt")
        self.lift2_passenger_bt.setGeometry(QRect(10, 220, 385, 32))
        self.lift2_floorpick_bt = QPushButton(Dialog)
        self.lift2_floorpick_bt.setObjectName(u"lift2_floorpick_bt")
        self.lift2_floorpick_bt.setGeometry(QRect(10, 260, 386, 32))
        self.lift1_label = QLabel(Dialog)
        self.lift1_label.setObjectName(u"lift1_label")
        self.lift1_label.setGeometry(QRect(100, 30, 201, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 190, 201, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lift1_floorpick_bt.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043b\u0438\u0444\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435..", None))
        self.lift1_passenger_bt.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432 \u043d\u0430 \u044d\u0442\u0430\u0436\u0430\u0445", None))
        self.lift2_passenger_bt.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432 \u043d\u0430 \u044d\u0442\u0430\u0436\u0430\u0445", None))
        self.lift2_floorpick_bt.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043b\u0438\u0444\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435..", None))
        self.lift1_label.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0444\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u043e\u0434\u044a\u0435\u0437\u0434\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0444\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u043e\u0434\u044a\u0435\u0437\u0434\u0430:", None))
    # retranslateUi

    def lift1_passenger_bt_clicked(self):
        self.passenger_window_1.show()

    def lift2_passenger_bt_clicked(self):
        self.passenger_window_2.show()

    def set_house(self, house):
        self.house = house
        self.house.elevator1_moved_signal.connect(self.lift1_moved)
        self.house.elevator2_moved_signal.connect(self.lift2_moved)

    def lift1_save_all_passenger(self, passengers):
        for i in range(0, 9):
            self.house.add_passangers_to_floor(0, i, passengers[i])
            self.display_window.set_passengers_lift1(passengers[i], i)

    def lift2_save_all_passenger(self, passengers):
        for i in range(0, 9):
            self.house.add_passangers_to_floor(1, i, passengers[i])
            self.display_window.set_passengers_lift2(passengers[i], i)

    def lift1_floorpick_bt_clicked(self):
        self.floorpick_window_1.show()

    def lift2_floorpick_bt_clicked(self):
        self.floorpick_window_2.show()

    def lift1_called(self, t):
        self.house.call_elevator(0, t[0], t[1])

    def lift2_called(self, t):
        self.house.call_elevator(1, t[0], t[1])

    def lift1_moved(self, floor_num):
        self.display_window.change_elevator_floor(0, floor_num)

    def lift2_moved(self, floor_num):
        self.display_window.change_elevator_floor(1, floor_num)