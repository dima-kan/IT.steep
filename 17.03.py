# Є текстовий файл. Виведіть кількість рядків та кількість
# символів в ньому

# #
# with open("text.txt",encoding="UTF-8") as file:
#     text = file.read()
#
#
# print(len(text))
# count_lines = text.count("\n") + 1
# print(count_lines)
# print(text)

# Користувач вводить ім’я та вік. Запишіть їх у файл. Назву
# файлу також вводить користувач(без розширення .txt)


# age = int(input("Введіть вік "))
# name = input("Введіть ім’я ")
# filename = input("Введіть назву файлу: ")
#
#
# with open(filename + ".text", "w" ) as file:
#     file.write(name)
#     file.write("\n")
#     file.write(str(age))


# Є текстовий файл. Запишіть його рядки в інший файл

# with open("text.txt", encoding="UTF-8") as file:
#     text = file.readlines()
#
# with open("text1.txt", "w", encoding="UTF-8") as file:
#     file.writelines(text)


# вдання 4
# Користувач вводить літеру та назву файлу. Виведіть усі
# слова з файлу, які починаються на цю літеру.


# letter = input("Введіть букву")
# file_name = input("Введіть назву файлу")
# file_name = file_name + ".txt"
# with open(file_name, encoding="UTF-8") as file:
#     text = file.read()
#
# words = text.split("\n")
# words = "".join(words)
# words = words.split(" ")
# for word in words:
#     if word.startswith(letter):
#         print(word)


# Є текстовий файл. Замініть у ньому усі символи * на &, та
# навпаки.


# with open("text1.txt", encoding="UTF-8") as file:
#     text = file.read()
#
# new_text = ""
#
# for sym in text:
#     if sym == "*":
#         new_text += "&"
#     elif sym == "&":
#         new_text += "*"
#     else:
#         new_text += sym
#
# with open("text1.txt", "w", encoding="UTF-8") as file:
#     file.write(new_text)


# Завдання 6
# Напишіть функцію, яка отримує назву файлу та список
# Практичне завдання
# чисел як параметри. Потрібно записати всі числа у файл,
# розмістивши кожне число на окремому рядку.
# Напишіть іншу функцію, яка отримує назву файл та читає
# з нього ці числа і повертає як список.
