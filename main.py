import sys
from PyQt5.QtCore import QTimer
from control_window import *


class Passenger:
    def __init__(self, destination_floor):
        self.destination_floor = destination_floor


class Elevator(QObject):
    new_floor_signal = pyqtSignal(int)
    move_further_signal = pyqtSignal()
    elevator_arrived_signal = pyqtSignal(int)
    passengers_left_signal = pyqtSignal(int)

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
        self.move_further_signal.connect(self.move)

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def move(self):
        print('move called')
        self.timer.stop()
        if self.current_floor == 0 and self.direction == -1 or self.current_floor == 8 and self.direction == 1:
            self.direction = 0

            # self.passengers_left_signal.emit(len(self.passengers))
        elif self.called:
            if self.current_floor != self.target_floor:
                self.timer.start(self.timeout)
            else:
                self.timer.stop()
                self.called = False
                self.elevator_arrived_signal.emit(self.current_floor)
        else:
            if len(self.passengers) == 0:
                self.timer.stop()
                self.direction = 0
            else:
                self.timer.start(self.timeout)

    def __change_floor(self):
        print('change floor')
        self.timer.stop()
        if self.direction == 1:
           self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1
        self.new_floor_signal.emit(self.current_floor)
        if self.called:
            self.move_further_signal.emit()

        elif not self.called and (len(self.passengers) < self.capacity):
            if self.__check_floor_for_passengers():
                self.passengers_left_signal.emit(self.__passengers_leave())
            self.elevator_arrived_signal.emit(self.current_floor)

        elif not self.called and self.__check_floor_for_passengers():
            self.passengers_left_signal.emit(self.__passengers_leave())
            self.elevator_arrived_signal.emit(self.current_floor)
        elif not self.called and not self.__check_floor_for_passengers():
            self.move_further_signal.emit()


        print('change floor - emit done')

    def __passengers_leave(self):
        count = 0
        tmp_list = []
        for i in self.passengers:
            if i.destination_floor == self.current_floor:
                count += 1
            else:
                tmp_list.append(i)
        self.passengers = tmp_list
        return count

    def __check_floor_for_passengers(self):
        for i in self.passengers:
            if i.destination_floor == self.current_floor:
                return True
        return False

    def change_direction(self, direction):
        self.direction = direction

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

    def set_passengers(self, passengers):
        self.num_passengers_up = passengers[0]
        self.num_passengers_down = passengers[1]

    def add_passengers(self, passengers):
        self.num_passengers_up += passengers[0]
        self.num_passengers_down += passengers[1]


class House(QObject):
    elevator1_moved_signal = pyqtSignal(int)
    elevator2_moved_signal = pyqtSignal(int)
    elevator1_arrived_signal = pyqtSignal(tuple)
    elevator2_arrived_signal = pyqtSignal(tuple)
    elevator1_passengers_left_signal = pyqtSignal(int)
    elevator2_passengers_left_signal = pyqtSignal(int)

    def __init__(self, num_elevators, num_floors, elevator_capacity):
        super().__init__()
        self.elevators = [Elevator(elevator_capacity) for _ in range(num_elevators)]
        self.floors = [[Floor(number) for number in range(1, num_floors + 1)],
                       [Floor(number) for number in range(1, num_floors + 1)]]

        self.elevators[0].new_floor_signal.connect(self.elevator_1_moved)
        self.elevators[1].new_floor_signal.connect(self.elevator_2_moved)
        self.elevators[0].elevator_arrived_signal.connect(self.elevator1_arrived)
        self.elevators[1].elevator_arrived_signal.connect(self.elevator2_arrived)
        self.elevators[0].passengers_left_signal.connect(self.elevator1_passengers_left_signal)
        self.elevators[1].passengers_left_signal.connect(self.elevator2_passengers_left_signal)

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
        self.elevators[elevator_num].called = True
        self.elevators[elevator_num].target_floor = floor_number
        self.elevators[elevator_num].move()
        print("call_elev from house")


        return True

    def start_moving_elevator(self, elevator_num):
        self.elevators[elevator_num].move()

    def elevator_1_moved(self, floor_num):
        print('elev 1 move')
        self.elevator1_moved_signal.emit(floor_num)

    def elevator_2_moved(self, floor_num):
        print('elev 2 move')
        self.elevator2_moved_signal.emit(floor_num)

    def add_passengers_to_elevator(self, elevator_num, passengers):
        for i in passengers:
            passenger = Passenger(i)
            self.elevators[elevator_num].add_passenger(passenger)

    def add_passangers_to_floor(self, elevator_num, floor, passangers):
        self.floors[elevator_num][floor].set_passengers(passangers)

    def elevator1_arrived(self, num_floor):
        if self.floors[0][num_floor].call_up_button:
            if self.floors[0][num_floor].num_passengers_up > 0:
                self.floors[0][num_floor].call_up_button = False
                self.elevators[0].change_direction(1)
                direction = 1
                self.elevator1_arrived_signal.emit((num_floor, direction,
                                                    min(self.floors[0][num_floor].num_passengers_up,
                                                        self.elevators[0].capacity)
                                                    ))
        elif self.floors[0][num_floor].call_down_button:
            if self.floors[0][num_floor].num_passengers_down > 0:
                self.floors[0][num_floor].call_down_button = False
                self.elevators[0].change_direction(-1)
                direction = -1
                self.elevator1_arrived_signal.emit(
                    (num_floor, direction, min(self.floors[0][num_floor].num_passengers_down,
                                               self.elevators[0].capacity)))
        else:
            if self.elevators[0].direction == 1:
                if self.floors[0][num_floor].num_passengers_up > 0:
                    self.elevator1_arrived_signal.emit(
                        (num_floor, self.elevators[0].direction, min(self.floors[0][num_floor].num_passengers_up,
                                                                     self.elevators[0].capacity - len(
                                                                         self.elevators[0].passengers)))
                    )
                elif len(self.elevators[0].passengers) != 0:
                    self.start_moving_elevator(0)
                elif len(self.elevators[0].passengers) == 0:
                    self.elevators[0].direction = 0
            else:
                if self.floors[0][num_floor].num_passengers_down > 0:
                    self.elevator1_arrived_signal.emit(
                        (num_floor, self.elevators[0].direction, min(self.floors[0][num_floor].num_passengers_down,
                                                                     self.elevators[0].capacity - len(
                                                                         self.elevators[0].passengers)))
                    )
                elif len(self.elevators[0].passengers) != 0:
                    self.start_moving_elevator(0)
                elif len(self.elevators[0].passengers) == 0:
                    self.elevators[0].direction = 0

    def elevator2_arrived(self, num_floor):
        if self.floors[1][num_floor].call_up_button:
            if self.floors[1][num_floor].num_passengers_up > 0:
                self.floors[1][num_floor].call_up_button = False
                self.elevators[1].change_direction(1)
                direction = 1
                self.elevator2_arrived_signal.emit((num_floor, direction,
                                                    min(self.floors[1][num_floor].num_passengers_up,
                                                        self.elevators[1].capacity)))
        elif self.floors[1][num_floor].call_down_button:
            if self.floors[1][num_floor].num_passengers_down > 0:
                self.floors[1][num_floor].call_down_button = False
                self.elevators[1].change_direction(-1)
                direction = -1
                self.elevator2_arrived_signal.emit((num_floor, direction,
                                                    min(self.floors[1][num_floor].num_passengers_down,
                                                        self.elevators[1].capacity)))
        else:
            if self.elevators[1].direction == 1:
                if self.floors[1][num_floor].num_passengers_up > 0:
                    self.elevator2_arrived_signal.emit(
                        (num_floor, self.elevators[1].direction, min(self.floors[1][num_floor].num_passengers_up,
                                                                     self.elevators[1].capacity - len(
                                                                         self.elevators[1].passengers)))
                    )
                elif len(self.elevators[1].passengers) != 0:
                    self.start_moving_elevator(1)
                elif len(self.elevators[1].passengers) == 0:
                    self.elevators[0].direction = 0
            else:
                if self.floors[1][num_floor].num_passengers_down > 0:
                    self.elevator2_arrived_signal.emit(
                        (num_floor, self.elevators[1].direction, min(self.floors[1][num_floor].num_passengers_down,
                                                                     self.elevators[1].capacity - len(
                                                                         self.elevators[1].passengers)))
                    )
                elif len(self.elevators[1].passengers) != 0:
                    self.start_moving_elevator(1)
                elif len(self.elevators[1].passengers) == 0:
                    self.elevators[0].direction = 0

    def elevator_1_passengers_left(self, num_people):
        self.elevator1_passengers_left_signal.emit(num_people)

    def elevator_2_passengers_left(self, num_people):
        self.elevator2_passengers_left_signal.emit(num_people)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    house = House(num_elevators=2, num_floors=9, elevator_capacity=4)
    # elevator_control_system = ElevatorControlSystem(house)

    control_window = ControlWindow()
    control_window.set_house(house)
    control_window.show()

    sys.exit(app.exec_())
