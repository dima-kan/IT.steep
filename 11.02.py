# Напишіть функцію, яка повертає добуток чисел з списку.
# Список передається як параметр.

# def multiplication_list(nums):
#     total = 1
#     for num in nums:
#         total *= num
#     return total
#
# print(multiplication_list([2, 3, 4]))

# Напишіть функцію, яка повертає найменше число з
# списку. Список передається як параметр.


# def min_list(items):
#     return min(items)
# print(min_list([2, 3, 4]))

# Напишіть функцію, яка повертає кількість парних
# чисел з списку. Список передається як параметр.


# def even_numbers(lst):
#     even = []
#     for num in lst:
#         if num % 2 == 0:
#             even.append(num)
#     return even
# print(even_numbers([1,2,3,4,5,6]))

# Напишіть функцію, яка видаляє з списку певне число.
# Якщо число повторюється, то треба видалити всі входження.
# Функція повинна повернути кількість видалених елементів.
# Список та число передаються як параметр
# def remove_all_occurrences(arr, num):
#     new_arr = arr.copy()
#     removed = 0
#
#     for item in arr:
#         if item == num:
#             removed += 1
#             new_arr.remove(item)
#
#     return removed
#
# print(remove_all_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

# Напишіть функцію, яка отримує два списи як параметри.
# Функція повинна об’єднати списки та повернути результат.
# Наприклад, якщо функція отримує списки [1, 2, 3] та [3, 4]
# то результатом має бути список [1, 2, 3, 3, 4

# def merge_lists(list1, list2):
#     return list1 + list2
#
# print(merge_lists([5,6,7,7,4],[1,2,3,4,5]))

# Напишіть функцію, яка підносить кожен елемент списку
# до степеня. Результатом має бути список з степенями всіх
# чисел. Список та показник степеня передаються як параметри

# def power_list(nums, exponent):
#     result = []
#     for num in nums:
#         result.append(num ** exponent)
#     return result
# print(power_list([1,2,3],2))
