# воріть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


# class Project:
#     def __init__(self, name: str, budget: int):
#         self.name = name
#         self.budget = budget
#
#         self.expenses: int = 0
#         self.is_end: bool = False
#         self.time: int = 0
#         self.tasks: List[str] = []
#
#     def show_info(self):
#         print(f"Project: {self.name}")
#         print(f"Budget: {self.budget}")
#         print(f"Expenses: {self.expenses}")
#         print(f"Remaining budget: {self.budget - self.expenses}")
#         print(f"Time: {self.time} months")
#         print(f"Completed: {self.is_end}")
#
#         print("\nTasks:")
#         if self.tasks:
#             for i, task in enumerate(self.tasks, 1):
#                 print(f"{i}. {task}")
#         else:
#             print("No tasks")
#
#     def get_new_task(self, task: str):
#         self.tasks.append(task)
#
#     def decompose(self, task: str, some_tasks: List[str]):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             self.tasks.extend(some_tasks)
#         else:
#             print("Task not found")
#
#     def complete_task(self, task: str, time: int, budget: int):
#         self.tasks.remove(task)
#         self.expenses += budget
#         self.time += time
#
#     def add_budget(self, amount: int):
#         self.budget += amount
#
# project1 = Project("Website", 5000)
#
# project1.get_new_task("Frontend")
# project1.get_new_task("Backend")
#
# project1.decompose("Frontend", ["HTML", "CSS", "JS"])
#
# project1.complete_task("HTML", 1, 500)
# project1.complete_task("CSS", 1, 400)
#
# project1.add_budget(1000)
#
# project1.show_info()


# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон


class Phone:
    def __init__(self, max_memory):
        self.max_memory = max_memory
        self.used_memory: int = 0
        self.is_on: bool = False
        self.apps: dict[str, int] = {}

    def show_info(self):
        print("Інформація про телефон:")
        print(f"Максимальна пам’ять: {self.max_memory}")
        print(f"Зайнята пам’ять: {self.used_memory}")
        print(f"Стан: {'Увімкнений' if self.is_on else 'Вимкнений'}")
        print("Додатки:")

        if not self.apps:
            print("  Немає встановлених додатків")
        else:
            for name, memory in self.apps.items():
                print(f"  {name}: {memory} МБ")

    def install_app(self, name, memory):
        if self.used_memory + memory > self.max_memory:
            print("Недостатньо пам’яті")
            return
        self.apps[name] = memory
        self.used_memory += memory

    def remove_app(self, name):
        if name in self.apps:
            self.used_memory -= self.apps[name]
            del self.apps[name]
            print(f"Додаток '{name}' видалено.")


phone = Phone(128)
phone.install_app("TG", 20)
phone.remove_app("TG")
phone.show_info()
