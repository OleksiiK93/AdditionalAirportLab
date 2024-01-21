class Airport:
    def __init__(self, name) -> None:
        self.name = name
        self.departure_lounge = []

    def add_passenger(self, passenger):
        self.departure_lounge.append(passenger)

    def remove_passenger(self, passenger):
        self.departure_lounge.remove(passenger)

    def boarding(self, plane):
        passengers_to_board = list(self.departure_lounge)
        for passenger in passengers_to_board:
            plane.add_passenger(passenger)
            if passenger in plane.passengers:
                self.remove_passenger(passenger)