import sys
from PyQt5.QtCore import QTimer
from control_window import *


class Passenger:
    def __init__(self, destination_floor):
        self.destination_floor = destination_floor


class Elevator(QObject):
    new_floor_signal_for_lift = pyqtSignal()
    new_floor_signal_for_house = pyqtSignal(int)
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.current_floor = 0
        self.direction = 0  # 0 for stop, 1 for up, -1 for down
        self.passengers = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.__change_floor)
        self.target_floor = 0
        self.called = False
        # self.timer.start(1000)
        self.timeout = 1000
        self.new_floor_signal_for_lift.connect(self.move)


    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def move(self):
        print('move called')
        self.timer.stop()
        if self.current_floor != self.target_floor:
            self.timer.start(self.timeout)
      #  else:
       #     self.timer.stop()
    # todo emit


    def __change_floor(self):
        print('change floor')
        #self.timer.stop()
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1
        self.new_floor_signal_for_lift.emit()
        self.new_floor_signal_for_house.emit(self.current_floor)
        print('change floor - emit done')


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


class House(QObject):
    elevator1_moved_signal = pyqtSignal(int)
    elevator2_moved_signal = pyqtSignal(int)
    def __init__(self, num_elevators, num_floors, elevator_capacity):
        super().__init__()
        self.elevators = [Elevator(elevator_capacity) for _ in range(num_elevators)]
        self.floors = [[Floor(number) for number in range(1, num_floors + 1)], [Floor(number) for number in range(1, num_floors + 1)]]

        self.elevators[0].new_floor_signal_for_house.connect(self.elevator_1_moved)
        self.elevators[1].new_floor_signal_for_house.connect(self.elevator_2_moved)



    def call_elevator(self, elevator_num, floor_number, direction):
        if self.elevators[elevator_num].direction != 0:
            return False
        else:
            if floor_number > self.elevators[elevator_num].current_floor:
                self.elevators[elevator_num].direction = 1
            elif floor_number < self.elevators[elevator_num].current_floor:
                self.elevators[elevator_num].direction = -1
        if direction == 1:
            self.floors[elevator_num][floor_number].call_up_button = True

        elif direction == -1:
            self.floors[elevator_num][floor_number].call_down_button = True
        self.elevators[elevator_num].target_floor = floor_number
        self.elevators[elevator_num].move()
        print("call_elev from house")


        return True

    def elevator_1_moved(self, floor_num):
        print('elev 1 move')
        self.elevator1_moved_signal.emit(floor_num)

    def elevator_2_moved(self, floor_num):
        print('elev 2 move')
        self.elevator2_moved_signal.emit(floor_num)

    def add_passangers_to_floor(self, elevator_num, floor, passangers):
        self.floors[elevator_num][floor].add_passengers(passangers)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    house = House(num_elevators=2, num_floors=9, elevator_capacity=4)
    # elevator_control_system = ElevatorControlSystem(house)


    control_window = ControlWindow()
    control_window.set_house(house)
    control_window.show()


    sys.exit(app.exec_())

