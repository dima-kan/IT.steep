# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.


# def get_password():
#     password = input("Введіть пароль: ")
#     if len(password) < 8:
#         raise ValueError("Пароль містить менше 8 символів")
#
#     if len(set(password)) != len(password):
#         raise ValueError("Пароль містить однакові символи")
#
#     return password
#
#
# try:
#     password = get_password()
#     print(password)
# except ValueError as err:
#     print("Помилка", err)

# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану
# функцію


# users = {
#     "admin": "12345678",
#     "user1": "qwerty12",
#     "user2": "password9"
# }
#
# def check_login(users):
#     password = input("Please enter your password: ")
#     login = input("Please enter your username: ")
#
#     if not login in users or users[login] != password:
#         raise ValueError("Invalid username or password")
#
#     return users
#
# try:
#     print(check_login(users))
# except ValueError as err:
#     print("Помилка", err)
