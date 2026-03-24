# Є кортеж з назвами міст. Виведіть ті міста, які
# зустрічаються в кортежі більше одного разу

# cities = ("Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro", "Kyiv", "Lviv")
#
# cities1 = ()
# city = ()
#
# for city in cities:
#     if cities.count(city) > 1:
#         cities1 += (city,)
#

# print(cities1)
# # Є два кортежі з випадковими числами. Виведіть на екран
# # ті числа, які є в першому кортежі, але немає в другому.
#
#
#
# tuple1 = tuple(random.randint(1, 100) for _ in range(5))
# tuple2 = tuple(random.randint(1, 100) for _ in range(5))
#
# print(tuple1)
# print(tuple2)
#
# result = []
#
# for num in tuple1:
#     if num not in tuple2:
#         if num not in result:
#             result.append(num)
#
# print(result)
#
#


# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()
# def common_elements_by_index(tuple1, tuple2):
#
#     result = []
#     for item1, item2 in zip(tuple1, tuple2):
#         if item1 == item2:
#             result.append(item1)
#
#     return result
