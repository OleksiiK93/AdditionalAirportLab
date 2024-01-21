class Person:
    def __init__(self, name, age, boarding_pass, cash, airport) -> None:
        self.name = name
        self.age = age
        self.boarding_pass = boarding_pass
        self.cash = cash
        self.airport = airport
    
    def buy_stuff(self, product_name):
        if product_name in self.airport.shop:
            if self.airport.shop[product_name] <= self.cash:
                self.cash -= self.airport.shop[product_name]
            else:
                print(f'{self.name} doesn\'t have enought money to buy {product_name}.')
        else:
            print(f'Sorry, {product_name} isn\'t available at {self.airport.name} at this time.')