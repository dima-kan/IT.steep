# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик


# class Cart:
#     def __init__(self, client:str, items:list):
#         self.client = client
#         self.items = items
#
#     def add_item(self, item):
#         self.items.append(item)
#         print(f"Товар '{item}' додано до кошика.")
#
#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"Товар '{item}' видалено з кошика.")
#         else:
#             print(f"Товар '{item}' не знайдено в кошику.")
#
#     def show_cart(self):
#         print(f"Клієнт: {self.client}")
#         print("Кошик:", self.items)
#
#
# cart = Cart("Дмитро", [])
#
# cart.add_item("Хліб")
# cart.add_item("Молоко")
#
# cart.show_cart()
#
# cart.remove_item("Хліб")
#
# cart.show_cart()

# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.


class Phone:
    def __init__(self, number, battery_level=100):
        self.number = number
        self.battery_level = battery_level

    def decrease_battery(self, percent):
        self.battery_level -= percent
        if self.battery_level < 0:
            self.battery_level = 0

        if self.battery_level < 20:
            print("Заряд батареї менше 20%! Підключіть телефон до зарядки.")

    def show_info(self):
        print(f"Номер телефону: {self.number}")
        print(f"Рівень заряду: {self.battery_level}%")


phone = Phone("+380123456789", 50)

phone.show_info()
phone.decrease_battery(35)
phone.show_info()
