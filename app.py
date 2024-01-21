from person import Person
from plane import Plane

person_1 = Person('Oleksii', 30)
person_2 = Person('Paul', 18)
person_3 = Person('Helga', 49)

plane = Plane('Airbus', 'ZZ89', 2)

print(f'The plane on flight {plane.flight_number} is an {plane.type} with capacity of {plane.capacity}.')
plane.add_passenger(person_1)
plane.add_passenger(person_2)
plane.add_passenger(person_3)
print(f'Even though three people tried to get aboard, due to its limited capacity there are only {len(plane.passengers)} people permitted on the flight.')
plane.remove_passenger(person_1)
print(plane.passengers[0].__dict__)
plane.clear_passengers()
print(plane.passengers)