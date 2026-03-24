# Напишіть функцію для обрахунку температури склянки
# води, яку помістили в холодильник через деякий час
# Параметри:
# T_env – температура в холодильнику
# T0 – початкова температура води
# t – час у секундах проведений в холодильнику
# k – коефіцієнт охолодження, за замовчуванням 0.05
# Формула для обрахунку:
#  ( ) ( )
# Див math.exp()

#
# import math
#
# def calculate_water_temperature(t0, t_env, t, k = 0.05):
#     t_new = t_env+(t0-t_env)*math.exp(-k*t)
#     return t_new
#
# if __name__ == "__main__":
#     result = calculate_water_temperature(80, 4, 60)
#     print(f"Температура води: {result:.2f}°C")


# Завдання 2
# Напишіть функцію з параметром show_time, яка запитує в
# користувача ім’я та повертає його.
# Якщо show_time = True, то функція повинна вивести на
# екран час своєї роботи у секундах.
# Див time.time()

# import time
#
# def get_username(show_time:bool = True):
#     name = input("Enter your name: ")
#     if show_time:
#         start_time = time.time()
#         end_time = time.time()
#         execution_time = end_time - start_time
#         return name,execution_time
# print(get_username())


# Напишіть власний модуль date_utils.py з функцією яка
# отримує дату дедлайну у форматі YYYY-MM-DD. Поверніть
# кількість днів яка залишилаь до дедлайна.
# Імпортуйте цей модуль в іншому файлі та використайте
# функцію, дедлайн вводить користувач. Якщо залишилось
# менше тижня до кінця дедлайна, виведіть відповідне
# повідомлення.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days


from date_utils import days_until_deadline

user_input = input("Введіть дату дедлайну (YYYY-MM-DD): ")

days_left = days_until_deadline(user_input)

if days_left > 0:
    if days_left < 7:
        print(f"Увага! До дедлайну залишилось менше тижня {days_left} днів)")
    else:
        print(f"До дедлайну залишилось {days_left} днів")
elif days_left < 0:
    print(f"Дедлайн минув {(days_left)} днів тому")
else:
    print("Дедлайн сьогодні!")
