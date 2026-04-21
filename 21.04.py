from abc import ABC
from enum import Enum


class AlertLevel(Enum):
    low = "low"
    middle = "middle"
    high = "high"


class CleaningMode(Enum):
    dry = "dry"
    wet = "wet"


class RobotStatus(Enum):
    off = "off"
    on = "on"


class Robot(ABC):
    def __init__(
        self, name: str, battery_level: int = 100, status: RobotStatus = RobotStatus.off
    ):
        self._name = name
        self._battery_level = battery_level
        self._status = status

    def info(self):
        print(f"Ім'я робота: {self._name}")
        print(f"Рівень заряду: {self._battery_level}%")
        print(f"Робот статус:{self._status}")

    def charge(self):
        self._battery_level = 100

    def turn_on(self):
        self._status = RobotStatus.on

    def turn_off(self):
        self._status = RobotStatus.off


class CleaningRobot(Robot):
    def __init__(
        self,
        cleaning_mode: CleaningMode,
        name: str,
        battery_level: int = 100,
        status: RobotStatus = RobotStatus.off,
        dust_capacity: int = 0,
        water_capacity: int = 100,
    ):
        super().__init__(name, battery_level, status)
        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity
        self._cleaning_mode = cleaning_mode

    def info(self):
        super().info()
        print(f"Контейнер пилу: {self._dust_capacity}%")
        print(f"Контейнер води: {self._water_capacity}%")
        print(f"Режим прибирання: {self._cleaning_mode}")

    def turn_on(self):
        if self._dust_capacity == 100:
            print(f"ПОМИЛКА: {self._name} - Контейнер для пилу повний!")
            return
        if self._water_capacity == 0 and self._cleaning_mode == CleaningMode.wet:
            print(f"ПОМИЛКА: {self._name} - Контейнер для води порожній!")
            return
        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0

    def fill_water(self):
        self._water_capacity = 100  # Fixed: should be 100, not 0

    def swap_mode(self):
        if self._cleaning_mode == CleaningMode.dry:
            self._cleaning_mode = CleaningMode.wet
            print(f"{self._name}: Режим змінено ")
        else:
            self._cleaning_mode = CleaningMode.dry
            print(f"{self._name}: Режим змінено")

    def clean(self, energy: int, dust: int, water: int | None = None):
        if self._status != RobotStatus.on:
            print(f"ПОМИЛКА: {self._name} - Робот вимкнено! ")
            return

        if self._battery_level < energy:
            print(f"ПОМИЛКА: {self._name} - Недостатньо заряду!")
            return

        if self._cleaning_mode == CleaningMode.dry:
            if self._dust_capacity + dust > 100:
                print(
                    f"ПОМИЛКА: {self._name} - Недостатньо місця в контейнері для пилу!"
                )
                return

            self._dust_capacity += dust
            self._battery_level -= energy
            print(f"{self._name}: Сухе прибирання завершено. ")

        else:
            if water is None:
                water = dust
            if self._water_capacity < water:
                print(f"ПОМИЛКА: {self._name} - Недостатньо води!")
                return

            if self._dust_capacity + dust > 100:
                print(
                    f"ПОМИЛКА: {self._name} - Недостатньо місця в контейнері для пилу!"
                )
                return

            self._dust_capacity += dust
            self._water_capacity -= water
            self._battery_level -= energy
            print(f"{self._name}: Вологе прибирання завершено.")


class SecurityRobot(Robot):
    def __init__(
        self,
        name: str,
        min_speed: int,
        alert_level: AlertLevel,
        dangerous_items: list[str] | None = None,
        battery_level: int = 100,
        status: RobotStatus = RobotStatus.off,
    ):
        super().__init__(name, battery_level, status)

        self._alert_level = alert_level
        self._min_speed = min_speed

        if dangerous_items is None:
            self._dangerous_items: list[str] = []
        else:
            self._dangerous_items = dangerous_items

    def info(self):
        super().info()
        print(f"Мінімальна швидкість: {self._min_speed}")
        print(f"Рівень небезпеки: {self._alert_level.value}")
        print(f"Cписок небезпечних предметів: {self._dangerous_items}.")

    def turn_off(self):
        self._alert_level = AlertLevel.low
        super().turn_off()

    def add_dangerous_item(self, item: str):
        if item not in self._dangerous_items:
            self._dangerous_items.append(item)

    def remove_dangerous_item(self, item: str):
        if item in self._dangerous_items:
            self._dangerous_items.remove(item)

    def detect(self, speed: int, item: str):
        if speed < self._min_speed:
            print(f"{self._name}: Швидкість занизька, ігноруємо")
            return

        if speed > self._min_speed:
            if self._alert_level != AlertLevel.high:
                self._alert_level = AlertLevel.middle

        if item in self._dangerous_items:
            self._alert_level = AlertLevel.high
            print(f"{self._name}: УВАГА! Виявлено небезпечний предмет: {item}")
            return

        print(f"{self._name}: Загрози не виявлено")
