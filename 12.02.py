# Напишіть функцію, яка отримує назву мови
# програмування та виводить повідомлення:
# «You are learning [мова програмування]»
# За замовчуванням, має бути Python.

# def learn_language(language="Python"):
#     print(f"You are learning {language}")
#

# learn_language(language="Python")
# learn_language()

# Напишіть функцію, яка отримує текст як параметр та
# виводить його на екран. Також має бути параметр
# lowercase:
#  Якщо він True, то текст потрібно перевести в
# нижній регістр
#  Якщо False, то текст не змінюється
# За замовчуванням False.


# def show_text(text,lowercase=False):
#     if lowercase:
#         text = text.lower()
#     return text
#
#
# print(show_text("Hello World",True))
# print(show_text(text="Hello World"))


# Напишіть функцію, яка отримує температуру та
# переводить її в градуси Цельсія або в Фаренгейта. Для
# цього є додатковий параметр unit_mapping:
#  Якщо він C_to_F, то функція повинна повернути
# градуси Фаренгейта
#  Якщо він F_to_C, то функція повинна повернути
# Практичне завдання
# градуси Цельсія
#  Якщо він щось інше, то функція виводить
# повідомлення про помилку, та повертає число без
# змін
# За замовчуванням, C_to_F


# def convert_temperature(temperature, unit_mapping="C_to_F"):
#     if unit_mapping == "C_to_F":
#         return temperature * 9 / 5 + 32
#
#     elif unit_mapping == "F_to_C":
#         return (temperature - 32) * 5 / 9
#
#     else:
#         print("Unknown unit mapping")
#         return temperature
#
#
# print(convert_temperature(45, unit_mapping="F_to_C"))
# print(convert_temperature(-45))


# Напишіть функцію, яка отримує список чисел як
# параметр та повертає кількість парних або непарних
# чисел в ньому, в залежності від параметра odd:
#  Якщо він True, то кількість непарних
#  Якщо False, то кількість парних
# За замовчуванням False.


# def count_numbers(items,odd=False):
#     odd_count = 0
#     even_count = 0
#     if odd:
#         for item in items:
#             if item % 2 != 0:
#                  odd_count+= 1
#     else:
#         for item in items:
#             if item % 2 == 0:
#                 even_count += 1
#     return odd_count, even_count
#

# print(count_numbers([1,2,3,4,5,6]))
# print(count_numbers([1,2,3,4,5,6], odd=True))


# Напишіть функцію, яка отримує декілька чисел як
# параметрів.
#  Якщо числа 2, то повернути найбільше
#  Якщо числа 3, то повернути суму
#  Якщо чисел більше 3, то повернути їхній добуток

#
# def process_numbers(*args):
#     total = 1
#     if len(args) == 2:
#         return max(args)
#
#     elif len(args) == 3:
#         return sum(args)
#
#     for num in args:
#         total *= num
#     return total
#
# print(process_numbers(1, 2, 5))
# print(process_numbers(1, 2, 3, 4))


#  Завдання 6 (ускладнене) — Операції над числом
# Умова:
# Напишіть функцію, яка отримує такі параметри:
#
# Число x.
# Рядковий параметр operation, що визначає дію.
# Числовий параметр power — степінь, до якої потрібно піднести число (за замовчуванням 2).
#
# Функція повинна:
#
# Якщо operation == "pow", повернути число x, піднесене до степеня power.
# Якщо operation == "abs", повернути модуль числа x.
# Якщо operation == "invert", повернути протилежне число, тобто -x.
# Якщо operation має інше значення, функція має:
#
# вивести повідомлення про помилку (у будь-якій зрозумілій формі),
# повернути None.


# def apply_operation(x, operation = "pow", power = 2):
#     if operation == "pow":
#         return pow(x,power)
#
#     elif operation == "abs":
#         return abs(x)
#
#     elif operation == "invert":
#         return -x
#
#     else:
#         print("Invalid operation")
#         return None
#
#
# print(apply_operation(7, operation="invert"))


# 🔹 Завдання 7 (ускладнене) — Обробка тексту з режимами
# Умова:
# Напишіть функцію, яка отримує:
# Рядок text.
# Рядковий параметр mode.
# Булевий параметр reverse_words (за замовчуванням False).
# Функція повинна виконувати такі дії:
# Спочатку обробити рядок text залежно від параметра mode:
# Якщо mode == "upper", перетворити всі символи рядка у верхній регістр.
# Якщо mode == "lower", перетворити всі символи у нижній регістр.
# Якщо mode == "capitalize", зробити перший символ великою літерою, а всі інші — малими.
# Якщо mode має будь-яке інше значення, рядок text залишається без змін.
# Після цього, якщо reverse_words == True, необхідно:
# розділити рядок на слова,
# перевернути порядок слів у рядку,
# зібрати їх назад в один рядок.
# Важливо: самі слова не змінюються, змінюється тільки їх порядок.
# Параметри за замовчуванням:
# mode == "lower".
# reverse_words == False.


def process_text(text: str, mode="lower", reverse_words=False):
    if mode == "upper":
        text = text.upper()
    elif mode == "lower":
        text = text.lower()

    elif mode == "capitalize":
        text = text.capitalize()

    else:
        pass

    if reverse_words:
        words = text.split()
        words.reverse()
        text = " ".join(words)
    return text
