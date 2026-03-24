# Користувач вводить числа через кому. Збережіть їх у
# кортеж. Виведіть на екран:
#  Суму чисел
#  Найбільше та найменше число
#  Перші та останні 3 числа
#  Кількість чисел 7
#  Пари індекс – число


# numbers = input("Введіть числа через кому: ").split(',')
# new_nums = []
#
# for num in numbers:
#     num = int(num)
#     new_nums.append(num)
#
# numbers_tuple = tuple(new_nums)
#
# print(sum(numbers_tuple))
# print(min(numbers_tuple), max(numbers_tuple))
# print(numbers_tuple[:3], numbers_tuple[-3:])
#
# total = 0
#
# for num in numbers_tuple:
#     if num == 7:
#         total +=1
# print(total)
#
#
# for index, number in enumerate(numbers_tuple):
#     print({index} , {number})


# Напишіть наступну програму: є кортеж з іменами
# зареєстрованих студентів. Користувач вводить ім’я студента
# після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній
# рядок


# students = ("Олександр", "Марія", "Іван", "Олена", "Дмитро")
#
# while True:
#     name = input("Введіть ім’я студента")
#
#     if name == "":
#         break
#
#     if name in students:
#         print("Студент зареєстрований ")
#     else:
#         print("Такого студента нема")


# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
# Практичне завдання
#  Якщо фільм знаходиться в першій половині кортежу,
# треба вивести ретро-фільм
#  Якщо в другій половині – сучасний фільм
#  Якщо один з останніх п'яти – новий фільм


# movies = (
#     "Inception",
#     "The Matrix",
#     "Interstellar",
#     "The Godfather",
#     "Pulp Fiction",
#     "The Dark Knight",
#
#     "Fight Club",
#     "Forrest Gump",
#     "The Shawshank Redemption",
#     "Gladiator",
#     "The Lord of the Rings: The Fellowship of the Ring",
#     "Titanic"
# )
#
# name = input("Введіть назву фільму ")
#
# if name not in movies:
#     print("Такого фільму нема ")
# elif name in movies[:6]:
#     print("Ретро-фільм")
# elif name in movies[-5:]:
#     print("Новий фільм")
# elif name in movies[7:]:
#     print("Сучасний фільм")


# вдання 4
# Напишіть функцію, яка отримує кортеж з назвами фруктів
# та слово. Потрібно повернути скільки разів дане слово
# зустрічається в кортежі(регістр неважливий). Складні назви
# теж враховуються. Приклад:
# ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")


def process_fruits(fruits, word="яблуко"):
    total = 0
    word_lower = word.lower()

    for fruit in fruits:
        if word_lower in fruit.lower():
            total += 1

    return total


fruits = ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")
print(process_fruits(fruits))
