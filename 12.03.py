# Є список з товарами. Користувач вводить індекс товару,
# який треба вивести. Обробіть виняток

#
# products = ["apple", "banana", "cherry","milk"]
#
# try:
#     index = int(input("Введіть індекс товару: "))
#     print("Товар",products[index])
#
# except  IndexError:
#     print("Помилка: такого індексу не існує")
#     print(f"Індекс повинен бути в межах від  0 до {len(products) - 1}")
#
# except ValueError:
#     print("Помилка: потрібно вести число")

# Напишіть функцію, яка запитує користувача вік та
# повертає його. Якщо вік неправильний(<0 або >130)
# викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.

# def get_age():
#     age  = int(input("Введіть ваш вік "))
#     if age < 0 or age > 130:
#         raise ValueError("Невірний вік !")
#     return age
#
# try:
#     age = get_age()
#     print("Ваш вік:",age)
# except ValueError as err:
#     print("Помилка:",err)
#

# апишіть функцію, яка запитує користувача номер
# телефону та повертає його. Якщо номер не вірний, тобто не
# починається з +038 або в ньому не 11 символів то викликати
# виняток ValueError.
# Написати код try … except який використовує дану
# функцію


# def get_phone():
#     phone  = input("Введіть номер телефону ")
#
#     if not phone.startswith("+380") or len(phone) != 11:
#         print(len(phone))
#         raise ValueError("Невірний формат телефону")
#
#     return phone
#
#
# try:
#     phone = get_phone()
#     print("Ваш номер телефону", phone)
# except ValueError as err:
#     print("Помилка",err)


# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Обробіть виняток коли категорії немає в словнику.


categories = {
    "fruits": {"apple", "banana", "orange"},
    "food": {"bread", "milk", "banana", "water"},
    "drinks": {"water", "juice", "milk"},
    "sweet": {"chocolate", "banana"},
}

try:
    cat1 = input("Введіть першу категорію: ")
    cat2 = input("Введіть другу категорію: ")

    products = categories[cat1] & categories[cat2]
    print(products)

except KeyError:
    print("Помилка: такої категорії немає")


# Організуйте базу даних «Співробітники». Усі дані мають
# зберігатись у словнику де ключ – ім’я людини, значення –
# зарплата. Реалізуйте такий функціонал(через функції):
#  Вивести дані на екран
#  Добавити співробітника
#  Видалити співробітника
#  Показати зарплату співробітника
#  Змінити зарплату співробітнику


employees = {"Dmytro": 20000, "John": 15000}


def show_all():
    for key, value in employees.items():
        print(f"{key}: {value}")


def add_employee(name, salary):
    if name in employees:
        raise ValueError("Працівник вже існує")

    employees[name] = salary

    return employees


def del_employee(name):
    if name not in employees:
        raise ValueError("Працівника не знайдено ")
    del employees[name]

    return employees


def show_salary(name):
    if name not in employees:
        raise ValueError("Працівника не знайдено")

    print(f"{name}: {employees[name]}")


def change_salary(name, salary):
    if name not in employees:
        raise ValueError("Працівника не знайдено")
    employees[name] = salary

    return employees


try:
    add_employee("Petro", 20000)
    show_salary("Petro")
    show_all()
    change_salary("Petro", 15000)
    del_employee("John")
except ValueError as e:
    print("Помилка", e)
