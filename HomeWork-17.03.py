# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)


# with open("text.txt", "r", encoding="UTF-8") as file:
#     text = file.read()
# print(len(text))
#
# count_lines = text.count("\n") + 1
#
# print(count_lines)
# count = 0
#
# for char in text :
#     if char.isdigit():
#         count += 1
# print(count)
#
#
# vowels = "aeiouAEIOU"
# count1 = 0
# for vowel in text :
#     if vowel in vowels:
#         count1 += 1
#
# print(count1)


# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.


# filename = input("Введіть назву файлу: ")
# word = input("Введіть слово")
#
# with open(filename + ".txt", "r",encoding="UTF-8" ) as file:
#     text = file.read()
#
# punctuation_marks = ".,!?"
#
# for mark in punctuation_marks:
#     text = text.replace(mark, " ")
#
# text = text.split()
#
# count = 0
# for words in text:
#     if words.lower() == word.lower():
#         count += 1
# print(count)


# Є текстовий файл. Видаліть з нього останній рядок
with open("text.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("text.txt", "w", encoding="utf-8") as f:
    f.writelines(lines[:-1])
