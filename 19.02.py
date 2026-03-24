# Напишіть власний модуль string_utils.py з наступними
# функціями:
#  Видалення знаків пунктуації з рядка: ,.?!;:
#  Підрахунок кількості голосних у рядку
#  Перевірка чи є рядок паліндромом(читається однаково
# задом наперед)
# Імпортуйте цей модуль в іншому файлі та використайте
# всі 3 функції.
# Додатково у файлі string_utils.py напишіть код перевірки
# роботи функцій: користувач вводить назву функції та рядок,
# потрібно вивести результат.
# Ця перевірка не повинна запускатись при імпорті в
# іншому файлі.

# import string_utils
#
# text = "Hello ,,,,World"
#
# print(string_utils.is_palindrome(text))
# print(string_utils.count_vowels(text))
# print(string_utils.remove_punctuation(text))

# Напишіть функцію для обрахунку площі трикутника по
# формулі
#  ( )
# Параметри функції: сторони a і b та кут . Функцію синус
# візьміть з модуля math
# Практичне завдання
# Примітка: якщо ви будете вводити кут у градусах, то
# перед тим як рахувати синус, його потрібно перевести у
# радіани
# Див math.radians()

# import math
#
# def triangle_area(a, b, angle_degrees):
#     angle_radians = math.radians(angle_degrees)
#     area = 0.5 * a * b * math.sin(angle_radians)
#
#     return area

# Напишіть функцію, яка обчислює суму чисел від 1 до 10
# млн. Виведіть час роботи програми.
# Див time.time()


# import time
#
# def calculate_sum_with_time():
#     start_time = time.time()
#
#     total = 0

#     for i in range(1, 10000001):
#         total += i
#
#     end_time = time.time()
#     execution_time = end_time - start_time
#
#     return total, execution_time
#
# print(calculate_sum_with_time())

# авдання 4
# Користувач вводить свою дату народження у форматі
# YYYY-MM-DD. Виведіть вік користувача.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

# from datetime import date
#
#
# def get_age_user(date_birth: str ):
#     date_birth = date.fromisoformat(date_birth)
#     today = date.today()
#     age = today.year - date_birth.year
#
#     return age
#
# date_birth = input('Введіть дату народження у форматі YYYY-MM-DD: ')
# res = get_age_user(date_birth)
# print(f"Вік користувача: {res} років")
