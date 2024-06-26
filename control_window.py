from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from display_window import DisplayWindow
from main import House
from passenger_window import PassengerWindow
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

        self.passenger_window_1 = PassengerWindow()
        self.passenger_window_2 = PassengerWindow()
        self.passenger_window_2.elevatorname_label.setText('Лифт подъезда 2')
        self.elevator1_passenger_bt.clicked.connect(self.elevator1_passenger_bt_clicked)
        self.elevator2_passenger_bt.clicked.connect(self.elevator2_passenger_bt_clicked)
        self.passenger_window_1.save_passenger_signal.connect(self.elevator1_save_all_passenger)
        self.passenger_window_2.save_passenger_signal.connect(self.elevator2_save_all_passenger)

        self.floorpick_window_1 = FloorPickWindow()
        self.floorpick_window_2 = FloorPickWindow()
        self.elevator1_floorpick_bt.clicked.connect(self.elevator1_floorpick_bt_clicked)
        self.elevator2_floorpick_bt.clicked.connect(self.elevator2_floorpick_bt_clicked)
        self.floorpick_window_1.elevator_called_signal.connect(self.elevator1_called)
        self.floorpick_window_2.elevator_called_signal.connect(self.elevator2_called)
        # self.

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 303)
        self.elevator1_floorpick_bt = QPushButton(Dialog)
        self.elevator1_floorpick_bt.setObjectName(u"elevator1_floorpick_bt")
        self.elevator1_floorpick_bt.setGeometry(QRect(10, 110, 386, 32))
        self.elevator1_passenger_bt = QPushButton(Dialog)
        self.elevator1_passenger_bt.setObjectName(u"elevator1_passenger_bt")
        self.elevator1_passenger_bt.setGeometry(QRect(10, 60, 386, 32))
        self.elevator2_passenger_bt = QPushButton(Dialog)
        self.elevator2_passenger_bt.setObjectName(u"elevator2_passenger_bt")
        self.elevator2_passenger_bt.setGeometry(QRect(10, 220, 385, 32))
        self.elevator2_floorpick_bt = QPushButton(Dialog)
        self.elevator2_floorpick_bt.setObjectName(u"elevator2_floorpick_bt")
        self.elevator2_floorpick_bt.setGeometry(QRect(10, 260, 386, 32))
        self.elevator1_label = QLabel(Dialog)
        self.elevator1_label.setObjectName(u"elevator1_label")
        self.elevator1_label.setGeometry(QRect(100, 30, 201, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 190, 201, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.elevator1_floorpick_bt.setText(QCoreApplication.translate("Dialog",
                                                                   u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043b\u0438\u0444\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435..",
                                                                   None))
        self.elevator1_passenger_bt.setText(QCoreApplication.translate("Dialog",
                                                                   u"\u0417\u0430\u0434\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432 \u043d\u0430 \u044d\u0442\u0430\u0436\u0430\u0445",
                                                                   None))
        self.elevator2_passenger_bt.setText(QCoreApplication.translate("Dialog",
                                                                   u"\u0417\u0430\u0434\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432 \u043d\u0430 \u044d\u0442\u0430\u0436\u0430\u0445",
                                                                   None))
        self.elevator2_floorpick_bt.setText(QCoreApplication.translate("Dialog",
                                                                   u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043b\u0438\u0444\u0442 \u043d\u0430 \u044d\u0442\u0430\u0436\u0435..",
                                                                   None))
        self.elevator1_label.setText(QCoreApplication.translate("Dialog",
                                                            u"\u041b\u0438\u0444\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u043e\u0434\u044a\u0435\u0437\u0434\u0430:",
                                                            None))
        self.label_2.setText(QCoreApplication.translate("Dialog",
                                                        u"\u041b\u0438\u0444\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u043e\u0434\u044a\u0435\u0437\u0434\u0430:",
                                                        None))

    # retranslateUi

    def elevator1_passenger_bt_clicked(self):
        self.passenger_window_1.show()

    def elevator2_passenger_bt_clicked(self):
        self.passenger_window_2.show()

    def set_house(self, house):
        self.house = house
        self.house.elevator1_moved_signal.connect(self.elevator1_moved)
        self.house.elevator2_moved_signal.connect(self.elevator2_moved)
        self.house.elevator1_arrived_signal.connect(self.elevator1_arrived)
        self.house.elevator2_arrived_signal.connect(self.elevator2_arrived)
        self.house.elevator1_passengers_left_signal.connect(self.elevator_1_passangers_left)
        self.house.elevator2_passengers_left_signal.connect(self.elevator_2_passangers_left)

    def elevator1_save_all_passenger(self, passengers):
        for i in range(0, 9):
            self.house.add_passangers_to_floor(0, i, passengers[i])
            self.display_window.set_passengers_elevator1(passengers[i], i)

    def elevator2_save_all_passenger(self, passengers):
        for i in range(0, 9):
            self.house.add_passangers_to_floor(1, i, passengers[i])
            self.display_window.set_passengers_elevator2(passengers[i], i)

    def elevator1_floorpick_bt_clicked(self):
        self.floorpick_window_1.show()

    def elevator2_floorpick_bt_clicked(self):
        self.floorpick_window_2.show()

    def elevator1_called(self, t):
        self.house.call_elevator(0, t[0], t[1])

    def elevator2_called(self, t):
        self.house.call_elevator(1, t[0], t[1])

    def elevator1_moved(self, floor_num):
        self.display_window.change_elevator_floor(0, floor_num)

    def elevator2_moved(self, floor_num):
        self.display_window.change_elevator_floor(1, floor_num)

    def elevator1_arrived(self, t):
        print('elevator 1 arrived')
        self.fp_windows_1 = []
        self.counter_1 = t[2]
        self.destinations_1 = []
        for i in range(t[2]):
            floor_passanger_window = FloorPassengerWindow(t[1], t[0])
            floor_passanger_window.passenger_label.setText('Выберите этаж назначения пассажира ' + str(i + 1))
            self.fp_windows_1.append(floor_passanger_window)
            if t[1] == 1:
                for j in range(t[0] + 1, 9):
                    floor_passanger_window.comboBox.addItem(str(j + 1))
            else:
                for j in range(t[0], 0, -1):
                    floor_passanger_window.comboBox.addItem(str(j))
            floor_passanger_window.show()
            floor_passanger_window.close_signal.connect(self.fp_window_closed_1)

    def elevator2_arrived(self, t):
        self.fp_windows_2 = []
        self.counter_2 = t[2]
        self.destinations_2 = []
        for i in range(t[2]):
            floor_passanger_window = FloorPassengerWindow(t[1], t[0])
            floor_passanger_window.passenger_label.setText('Выберите этаж назначения пассажира ' + str(i + 1))
            self.fp_windows_2.append(floor_passanger_window)
            if t[1] == 1:
                for j in range(t[0] + 1, 9):
                    floor_passanger_window.comboBox.addItem(str(j + 1))
            else:
                for j in range(t[0], 0, -1):
                    floor_passanger_window.comboBox.addItem(str(j))
            floor_passanger_window.show()
            floor_passanger_window.close_signal.connect(self.fp_window_closed_2)

    def fp_window_closed_1(self, t):
        self.counter_1 -= 1
        self.destinations_1.append(t[2])
        if self.counter_1 == 0:
            self.fp_windows_1.clear()
            self.display_window.change_passengers_elevator1(len(self.destinations_1), t[1], t[0])
            if t[0] == 1:
                self.house.floors[0][t[1]].add_passengers((-len(self.destinations_1), 0))
            else:
                self.house.floors[0][t[1]].add_passengers((0, -len(self.destinations_1)))
            self.display_window.change_elevator_num(0, len(self.destinations_1))
            self.house.add_passengers_to_elevator(0, self.destinations_1)
            self.house.start_moving_elevator(0)

    def fp_window_closed_2(self, t):
        self.counter_2 -= 1
        self.destinations_2.append(t[2])
        if self.counter_2 == 0:
            self.fp_windows_2.clear()
            self.display_window.change_passengers_elevator2(len(self.destinations_2), t[1], t[0])
            if t[0] == 1:
                self.house.floors[1][t[1]].add_passengers((-len(self.destinations_2), 0))
            else:
                self.house.floors[1][t[1]].add_passengers((0, -len(self.destinations_2)))
            self.display_window.change_elevator_num(1, len(self.destinations_2))
            self.house.add_passengers_to_elevator(1, self.destinations_2)
            self.house.start_moving_elevator(1)

    def elevator_1_passangers_left(self, num):
        self.display_window.change_elevator_num(0, -num)

    def elevator_2_passangers_left(self, num):
        self.display_window.change_elevator_num(1, -num)