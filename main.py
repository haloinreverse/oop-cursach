import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QSpinBox, QComboBox
from control_window import *


class ElevatorUI(QMainWindow):
    def __init__(self, elevator_control_system):
        super().__init__()
        self.elevator_control_system = elevator_control_system
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Elevator Control System")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.floor_spinboxes = []
        self.direction_combobox = QComboBox()
        self.direction_combobox.addItem("Up")
        self.direction_combobox.addItem("Down")

        self.call_button = QPushButton("Call Elevator")
        self.call_button.clicked.connect(self.call_elevator)

        self.label = QLabel("Elevator Control System")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        for i in range(len(self.elevator_control_system.house.floors)):
            floor_spinbox = QSpinBox()
            floor_spinbox.setMinimum(0)
            floor_spinbox.setMaximum(10)  # Change maximum value as needed
            self.floor_spinboxes.append(floor_spinbox)
            self.layout.addWidget(floor_spinbox)

        self.layout.addWidget(self.direction_combobox)
        self.layout.addWidget(self.call_button)
        self.central_widget.setLayout(self.layout)

    def call_elevator(self):
        floor = self.floor_spinboxes[len(self.elevator_control_system.house.floors) - 1].value()
        direction = 1 if self.direction_combobox.currentText() == "Up" else -1
        num_passengers = 0
        for floor_spinbox in self.floor_spinboxes[:-1]:
            num_passengers += floor_spinbox.value()
        if self.elevator_control_system.house.call_elevator(floor, direction, num_passengers):
            print("Elevator called successfully!")
        else:
            print("No available elevators for this request.")


class ElevatorControlSystem:
    def __init__(self, house):
        self.house = house
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_elevators)
        self.timer.start(1000)  # 1000 milliseconds = 1 second

    def move_elevators(self):
        self.house.move_elevators()


class Passenger:
    def __init__(self, destination_floor):
        self.destination_floor = destination_floor


class Elevator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_floor = 1
        self.direction = 0  # 0 for stop, 1 for up, -1 for down
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def move(self):
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1

    def open_doors(self):
        # Implementation for opening doors
        pass

    def close_doors(self):
        # Implementation for closing doors
        pass


class Floor:
    def __init__(self, number):
        self.number = number
        self.call_up_button = False
        self.call_down_button = False
        self.num_passengers_up = 0
        self.num_passengers_down = 0

    def add_passengers(self, passengers):
        self.num_passengers_up = passengers[0]
        self.num_passengers_down = passengers[1]


class House:
    def __init__(self, num_elevators, num_floors, elevator_capacity):
        self.elevators = [Elevator(elevator_capacity) for _ in range(num_elevators)]
        self.floors = [[Floor(number) for number in range(1, num_floors + 1)], [Floor(number) for number in range(1, num_floors + 1)]]

    def call_elevator(self, floor_number, direction, num_passengers):
        if direction == 1:
            self.floors[floor_number - 1].call_up_button = True
        elif direction == -1:
            self.floors[floor_number - 1].call_down_button = True

        for elevator in self.elevators:
            if elevator.direction == 0 or (elevator.direction == direction and elevator.current_floor == floor_number):
                passengers = [Passenger(floor_number) for _ in range(num_passengers)]
                for passenger in passengers:
                    if elevator.add_passenger(passenger):
                        if elevator.direction == 0:
                            elevator.direction = direction
                        return True
        return False

    def move_elevators(self):
        for elevator in self.elevators:
            if elevator.direction != 0:
                elevator.move()
                if elevator.current_floor == 1 or elevator.current_floor == len(self.floors):
                    elevator.direction = 0
                # Additional logic for opening/closing doors can be implemented here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    house = House(num_elevators=2, num_floors=9, elevator_capacity=4)
    # elevator_control_system = ElevatorControlSystem(house)


    control_window = ControlWindow()
    control_window.set_house(house)
    control_window.show()


    sys.exit(app.exec_())

