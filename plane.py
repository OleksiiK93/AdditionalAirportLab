class Plane:
    def __init__(self, type, flight_number, capacity) -> None:
        self.type = type
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
    
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def clear_passengers(self):
        self.passengers.clear()