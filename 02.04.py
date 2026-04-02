# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи
# import math
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#
#     def get_perimeter(self):
#         return 2 * (self._width + self._height)
#
#
#     def display_info(self):
#         print(f"Прямокутнык: width = {self._width},
#         height = {self._height},периметр={self._width * self._height}")
#
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#
#
#     def get_perimeter(self):
#         return 2 * math.pi * self._radius
#
#
#     def display_info(self):
#         print(f"Коло: radius = {self._radius},довжина кола={self.get_perimeter()}")
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#
#     def get_perimeter(self):
#         return self._a + self._b + self._c
#
#
#     def display_info(self):
#         print(f"Трикутник: a = {self._a}, b = {self._b},
#         c = {self._c},периметр = {self.get_perimeter()}")
#
#
# def create_figure():
#     figure_type = input("Введіть тип фігури")
#
#     if figure_type == "rectangle":
#         w = float(input("Width"))
#         h = float(input("Height"))
#         return Rectangle(w, h)
#
#     elif figure_type == "circle":
#         r = float(input("radius"))
#         return Circle(r)
#
#     elif figure_type == "triangle":
#         a = float(input("a"))
#         b = float(input("b"))
#         c = float(input("c"))
#         return Triangle(a, b, c)
#
#     else:
#         print("невідомий тип фігури")
#         return None
#
#
# figures = []
#
# for _ in range(3):
#     fig = create_figure()
#     if fig:
#         figures.append(fig)
# for f in figures:
#     f.display_info()


# вдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# Практичне завдання
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.


class Manager:
    def __init__(self, name, base_salary):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary


class Developer:
    def __init__(self, name, base_salary, work_experience):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience

    def get_salary(self):
        if self._work_experience > 4:
            return self._base_salary * 1.2
        return self._base_salary


class Intern:
    def __init__(self, name, base_salary):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary / 2


def create_workers():
    worker_type = input("Тип ")
    base_salary = float(input("Базова зарплата: "))

    if worker_type == "manager":
        return Manager(base_salary)

    elif worker_type == "developer":
        exp = int(input("Стаж: "))
        return Developer(base_salary, exp)

    elif worker_type == "inter":
        return Intern(base_salary)

    else:
        print("Невідомий тип")
        return None


workers = []

for _ in range(3):
    w = create_workers()
    if w:
        workers.append(w)

for w in workers:
    w.display_info()
