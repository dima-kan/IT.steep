# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального

import random


class Car:
    def __init__(self, brand: str, race: float, fuel: float):
        self.brand = brand
        self.race = race
        self.fuel = fuel
        self.fuel_consumption = 5.5
        self.is_works = True

    def get_start(self, distance: float):
        if self.is_works and distance <= (self.fuel / self.fuel_consumption) * 100:
            self.race += distance
            self.fuel -= distance * (self.fuel_consumption / 100)
            print(f"Машина проїхала {distance}  та рівень пального {self.fuel}")
        else:
            print("Машина зламана ")

    def car_status(self):
        if random.random() < 0.4:
            self.is_works = False

    def repair(self):
        if not self.is_works:
            self.is_works = True
        else:
            print("Машина не зламана")

    def add_fuel(self, fuel: float):
        if fuel > 0:
            self.fuel += fuel
            print(f"Заправлено {fuel} л. В баку {self.fuel}")
        else:
            print("Пальне не може бути від'ємним")
            return


car = Car("Toyota", 95000, 16)
car.add_fuel(5)
car.get_start(100)
