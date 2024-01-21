class Airport:
    def __init__(self, name) -> None:
        self.name = name
        self.departure_lounge = []
        self.shop = {
            "M&Ms": 5.00,
            "Shitty headphones": 400.00,
            "Mechanically reclaimed floor sweepings sandwich": 150.00,
            "Copy of Roger's Profanisaurus": 20.00
            }

    def add_passenger(self, passenger):
        self.departure_lounge.append(passenger)

    def remove_passenger(self, passenger):
        self.departure_lounge.remove(passenger)

    def embark_passengers(self, plane):
        passengers_to_board = []

        for passenger in self.departure_lounge:
            if passenger.boarding_pass == plane.flight_number:
                passengers_to_board.append(passenger)

        for passenger in passengers_to_board:
            plane.add_passenger(passenger)
            if passenger in plane.passengers:
                self.remove_passenger(passenger)