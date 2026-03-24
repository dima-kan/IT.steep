# Напишіть функцію, яка отримує 2 словника та об’єднує їх
# в один. Якщо ключі співпадають то потрібно додати
# відповідні їм значення.

# def merge_dicts(dict1, dict2):
#     dict3 ={}
#
#     for key,value in dict1.items():
#         dict3[key] = value
#
#     for key, value in dict2.items():
#         if key in dict3:
#             dict3[key] += value
#         else:
#             dict3[key] = value
#
#     return dict3
#
# print(merge_dicts({'a':1, 'b':2}, {'c':3, 'd':4, 'a':4}))


# Напишіть функцію, яка отримує словник та інвертує його,
# тобто повертає новий словник, де ключі та значення змінені
# місцями.
# def invert_dict(dict1):
#     dict2 = {}
#     for key, value in dict1.items():
#         dict2[value] = key
#     return dict2
#
# print(invert_dict({'a':1,'b':2,'c':3}))


# Користувач вводить назви товарів та їх ціни поки не введе
# порожній рядок. Збережіть дані у словник. Якщо користувач
# вводить товар повторно та треба додати стару та нову ціни.
# В кінці виведіть таблицею товар – ціна. Також виведіть
# загальну ціну.

# data = {}
#
# while True:
#     item = input("Введіть назву товару: ")
#     if item == "":
#         break
#
#     price = input("Введіть ціну товару: ")
#
#     price = int(price)
#
#     if item in data:
#         data[item] += price
#     else:
#         data[item] = price
#
# total = 0
#
# for item, price in data.items():
#     print(item, "-", price)
#     total += price
#
# print("Загальна сума:", total)


# апишіть функцію, яка отримує текст та повертає
# словник, де ключі – це слова, а значення – їхня кількість в
# тексті.
# Добавте параметр за замовчуванням який визначає, чи
# Практичне завдання
# значення в словнику будуть кількостями слів, чи
# частотою(відсотком від загальної кількості).


def word_statistics(text, percent=True) -> dict:
    words = text.split()
    stats = {}

    for word in words:
        if word in stats:
            stats[word] += 1
        else:
            stats[word] = 1

    if percent:
        total = len(words)
        for word in stats:
            stats[word] = stats[word] / total * 100

    return stats


print(word_statistics("cat dog cat"))
