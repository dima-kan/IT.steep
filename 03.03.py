# Користувач вводить числа через кому. Збережіть їх у
# множину. Також створіть власну множину з випадковими
# числами(12 шт). Виведіть наступну інформацію:
#  Максимальне та мінімальне число, введене
# користувачем, а також кількість чисел
#  Унікальні числа, введені користувачем, яких немає
# # серед випадкових
# #  Спільні числа, введені користувачем, які є серед
# # випадкових
# #  Усі числа, які є або в одній або в іншій множині
#
# import random
# numbers_set2 = set(random.randint(1, 100) for _ in range(12))
# print(len(numbers_set2))
# numbers = input("Введіть числа через кому: ").split(',')
# new_nums = []
#
# for num in numbers:
#     num = int(num)
#     new_nums.append(num)
#
# numbers_set = set(new_nums)
#
# #  Максимальне та мінімальне число, введене
# # користувачем, а також кількість чисел
# print(min(numbers_set), max(numbers_set), len(numbers_set))
#
# #  Унікальні числа, введені користувачем, яких немає
# # # серед випадкових
#
# print(numbers_set - numbers_set2)
# #  Спільні числа, введені користувачем, які є серед
# # випадкових
#
# print(numbers_set & numbers_set2)
# #  Усі числа, які є або в одній або в іншій множині
#
# print(numbers_set | numbers_set2)

# Напишіть функцію, яка отримує список гостей(гості
# можуть повторюватись) та назву події. Потрібно вивести
# запрошення для кожного гостя і лише один раз.ву


# def generate_unique_invitations(guests, event_name):
#     unique_guests = set(guests)
#     for guest in unique_guests:
#         print(f"Шановний(а) {guest}, запрошуємо Вас на подію '{event_name}'!")
# generate_unique_invitations(["Олександр", "Марія", "Іван", "Олена", "Дмитро"],["Новий рік "])

# Напишіть функцію, яка отримує два списки з назвами
# # товарів для покупок двох знайомих людей. Виведіть наступне
# # повідомлення:
# #  Товари, які можна купити разом
# # Практичне завдання
# #  Товари, які потрібні лише першій людині
# #  Товари, які потрібні лише другій людині


# def compare_shopping_lists(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#
#     common_items = (set1 & set2)
#     only_first = (set1 - set2)
#     only_second = (set2 - set1)
#     return common_items, only_first, only_second
#
# person1 = ["хліб", "молоко", "яйця", "сир", "яблука"]
# person2 = ["молоко", "сир", "ковбаса", "яблука"]
#
# result = compare_shopping_lists(person1, person2)

# Організатор конференції створив 3 списки учасників:
# зареєстровані, ті хто оплатив участь і ті хто підтвердив свою
# присутність
# Напишіть функцію, яка отримує ці 3 списки та виводить
# наступну інформацію:
#  Імена тих, хто зареєструвався, але не оплатив участь
#  Імена тих, хто підтвердив присутність, але не
# зареєстрований
#  Імена тих, хто оплатив участь, але не підтвердив
# присутність
#  Імена тих, хто зареєструвався і оплатив участь
#  Імена тих хто пройшов усі 3 етапи


def process_conference_participants(register, paid, conf):
    register = set(register)
    paid = set(paid)
    conf = set(conf)

    print(register - paid)

    print(conf - register)

    print(paid - conf)

    print(register | paid)

    print(conf | register | paid)


register = ["Anna", "Bohdan", "Iryna", "Maksym", "Olena", "Taras"]

paid = ["Anna", "Iryna", "Taras", "Dmytro"]

conf = ["Anna", "Maksym", "Dmytro", "Sofia"]

process_conference_participants(register, paid, conf)
