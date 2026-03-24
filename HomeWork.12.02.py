# Напишіть функцію, яка отримує ім’я студента та
# виводить повідомлення:
# «You are welcome, [студент]»
# За замовчуванням, має бути ваше ім’я


# def welcome_student(name="Kandaurov"):
#     print(f"You are welcome,{name} ")
#
#
# welcome_student(name="Kandaurov")
# welcome_student()


# вдання 2
# Напишіть функцію, яка отримує два числа як
# параметр та тип операції, що з ними можна зробити:
#  Якщо він add, то поверніть суму чисел
#  Якщо diff, то поверніть різницю чисел
#  Якщо mult, то поверніть добуток чисел
#  Якщо щось інше, виведіть інформацію про помилку
# За замовчуванням add.

# def calculate(num1, num2, operation="add"):
#     if operation == "add":
#         return num1 + num2
#     elif operation == "diff":
#         return num1 - num2
#     elif operation == "mult":
#         return num1 * num2
#     else:
#         return print("Operation not supported")
#
# print(calculate(1, 2, operation="add"))
# print(calculate(1, 2, operation="diff"))


# Напишіть функцію, яка отримує назву свята та імена
# декількох гостей. Виведіть кожному гостю
# повідомлення:
# «[ім’я], you are invited to [назва свята]»
# Домашнє завдання
# Якщо гостей немає, потрібно вивести повідомлення:
# «No guests»


# def send_invitations(party_name, *guests):
#
#     if not guests:
#         print("No guests")
#     else:
#         for guest in guests:
#             print(f"{guest}, you are invited to {party_name}")
#
#
# print(send_invitations("Birthday Party", "Olena", "Ivan", "Maria"))
# print(send_invitations("New Year Party"))
