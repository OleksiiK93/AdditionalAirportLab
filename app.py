from person import Person
from plane import Plane
from airport import Airport

airport = Airport('Glasgow International')
person_1 = Person('Oleksii', 30, 'ZZ89', 500.0, airport)
person_2 = Person('Paul', 18, 'EJ991', 20.5, airport)
person_3 = Person('Helga', 49, 'ZZ89', 150.98, airport)
plane = Plane('Airbus', 'ZZ89', 3)

# print(f'The plane on flight {plane.flight_number} is an {plane.type} with capacity of {plane.capacity}.')
# plane.add_passenger(person_1)
# plane.add_passenger(person_2)
# plane.add_passenger(person_3)
# print(f'Even though three people tried to get aboard, due to its limited capacity there are only {len(plane.passengers)} people permitted on the flight.')
# plane.remove_passenger(person_1)
# print(plane.passengers[0].__dict__)
# plane.clear_passengers()
# print(plane.passengers)

airport.add_passenger(person_1)
airport.add_passenger(person_2)
airport.add_passenger(person_3)

airport.boarding(plane)

# for passenger in plane.passengers:
#     print(passenger.__dict__)

# for passenger in airport.departure_lounge:
#     print(passenger.__dict__)

person_2.buy_stuff("Lego")
print(person_2.cash)