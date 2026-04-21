# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# Домашнє завдання
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5


from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self._name = name
        self._satiety = satiety
        self._energy = energy

    def sleep(self):
        self._energy = 100

    def eat(self, food_amount):
        self._satiety += food_amount
        if self._satiety > 100:
            self._satiety = 100

    @abstractmethod
    def play(self, activity_level):
        raise NotImplementedError

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self._satiety > 60:
            self._energy -= 2 * activity_level
            self._satiety -= activity_level
            if self._energy < 0:
                self._energy = 0
            if self._satiety < 0:
                self._satiety = 0

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self._energy > 30:
            print("грається з мишею")
        elif self._satiety > 40:
            print("ловить мишу")
        else:
            self.eat(20)


class Dog(Pet):
    def play(self, activity_level):
        if self._satiety > 15:
            self._energy -= activity_level // 2
            self._satiety -= activity_level // 2
            if self._energy < 0:
                self._energy = 0
            if self._satiety < 0:
                self._satiety = 0

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self._satiety > 10:
            self._energy -= 5
            print(f"{self._name} зловив м’яч! Енергія: {self._energy}")
