# Користувач вводить рядок англійською мовою. Порахуйте
# скільки в ньому голосних літер(aeuio)


# total = 0
# vowels = "aeiou"
#
# text = input("Введіть текст:")
#
# for char in text.lower():
#     if char in vowels:
#         total += 1
#
# print(total)


# користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне
# слово. Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT

# text = input("Введіть текст: ")
#
# while True:
#     word = input("Введіть слово: ")
#     if word == "EXIT":
#         break
#     elif word in text:
#         highlighted = text.replace(word, word.upper())
#         print(highlighted)
#     else:
#         print("Такого слова немає")
#         continue

# Користувач вводить текст. Порахуйте скільки в ньому
# речень


# text = input("Введіть текст: ")
# total = 0
#
# for char in text:
#     if char in '.!?':
#         total += 1
#
# print(f"Кількість речень: {total}")
