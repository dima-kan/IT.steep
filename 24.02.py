# square = lambda num: num * num
# print(square(5))


# Отримує довжини трикутника і повертає периметр


# calculateTrianglePerimeter = lambda a, b, c: a+b+c
# print(calculateTrianglePerimeter(4, 5, 6))


# Отримує прізвище та ім’я і повертає рядок у форматі
# «Прізвище, ім’я»


# format_name = lambda surname, name: f"{surname}, {name}"
# print(format_name("Шевченко", "Тарас"))


# Перевіряє чи є число парним


# is_even = lambda number: number % 2 == 0
# print(is_even(5))


# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел та повертає список з лише
# додатніми числами
#  Отримує список слів та повертає список слів, в яких
# більше ніж 3 літери
#  Отримує список слів та літеру і повертає список тих
# слів, які починаються на цю літеру(регістр
# неважливий)

# num_list = [-1, -2, -3, 4, 5, 6, -7, 8, -9]
#
# def get_positive_numbers(num_list):
#
#     return list(filter(lambda x: x > 0, num_list))
#
# positive_numbers = get_positive_numbers(num_list)
# print(positive_numbers)
#
#
# # Отримує список слів та повертає список слів, в яких
# # більше ніж 3 літери
#
#
# words = ["Apple", "banana", "Avocado", "cherry", "apricot"]
#
# def litters(words):
#     return list(filter(lambda word: len(word) > 3, words))
#
#
# # Отримує список слів та літеру і повертає список тих
# # слів, які починаються на цю літеру(регістр
# # неважливий)
#
#
# def litter_start(words, letter):
#     return list(filter(lambda word: word.lower().startswith(letter.lower()), words))
