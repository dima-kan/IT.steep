# Напишіть lambda-функції, які:
#  Множить число на -1
#  Перевіряє чи рядок непорожній

# 1
# print((lambda x: x * -1)(5))
# 2
# print((lambda x: x != "")(""))

# Напишіть функцію, яка використовуючи filter:
#  Отримує список чисел, рахує середнє арифметичне та
# повертає список з числами, які більші за середнє
#  Отримує список слів та повертає список слів, в яких
# рівно 4 літери


# def filter_above_average(numbers)->list:
#     average = sum(numbers) / len(numbers)
#     return list(filter(lambda x: x > average, numbers))
#
# nums = [1, 5, 8, 10, 3, 7]
# result = filter_above_average(nums)
# print(result)


# def filter_four_letter_words(words):
#     return list(filter(lambda word: len(word) == 4, words))
#
#
# words = ["сон", "книга", "дерево", "вода", "сонце", "міст", "небо"]
# result = filter_four_letter_words(words)
# print(result)


# Напишіть функцію, яка отримує літеру та список слів і
# знаходить слово зі списку, в якому найбільша кількість даної
# літери.

# def find_words_with_most_letter(letter, words):
#
#     if not words:
#         return []
#
#     max_count = max(map(lambda word: word.count(letter), words))
#
#     result = list(filter(lambda word: word.count(letter) == max_count, words))
#
#     return result
#
# words = ["банан", "ананас", "апельсин", "мандарин", "гарбуз"]
# print(find_words_with_most_letter("а", words))
