# def show_text ():
#     print(f"“Don't compare yourself with anyone in this world…")
#     print("if you do so, you are insulting yourself”")
#     print("Steve Jobs")
# show_text()


# Напишіть функцію, яка приймає два числа як параметри та
# # відображає всі непарні числа між ними.
# def show_odd_numbers (start, end):
#     for num in range(start , end + 1):
#         if num % 2 != 0:
#             print(num)
# show_odd_numbers(1,30)


# Напишіть функцію, яка відображає пустий(лише межі) або
# заповнений квадрат. Функція має приймати 3 параметри:
# довжину сторони, символ для заповнення та логічну змінну:
#  Якщо вона рівна True, то квадрат заповнений
#  Якщо False, то квадрат пустий

# def draw_square(side, char, filled):
#     if filled:
#         for _ in range(side):
#             print(char * side)
#     else:
#         if side == 1:
#             print(char)
#         else:
#             print(char * side)
#             for _ in range(side - 2):
#                 print(char + " " * (side - 2) + char)
#             print(char * side)
#
#
# draw_square(4,"*",True)

# Напишіть функцію, яка повертає найменше серед п’яти
# чисел. Числа передаються як параметри.

# def get_min_of_four (num1, num2, num3, num4):
#     result = min(num1,num2,num3,num4)
#     print(result)
#     return result
# get_min_of_four(4, 5, 6, 7)

# Напишіть функцію, яка повертає добуток чисел в певному
# діапазоні. Межі діапазону передаються як параметри. Якщо
# межі неправильні(наприклад числа від 10 до 5), то поміняйте
# їх місцями.

# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start
#
#     total = 0
#     for nums in range(start, end + 1):
#         total *= nums
#     print(total)
#     return total
# product_in_range(1, 10)

# Напишіть функцію, яка повертає кількість цифр у числі.
# Число передається як параметр. Наприклад, якщо передали
# число 3875, то функція повертає 4.

# def count_digits(number):
#     return len(str(number))
#
# print(count_digits(100))
