# Користувач вводить через кому список товарів. Виведіть
# цей список на екран, але без повторень назв товарів

# items = input("Введіть список товарів через кому: ").split(',')
# new_nums = []
#
# for item in items:
#     new_nums.append(item)
#
# item_set = set(new_nums)
# print(item_set)


# У магазині є два списки клієнтів: ті хто отримав знижкові
# купони, і ті хто ними скористався.
# Напишіть функцію, яка отримує 2 списки та виводить
# інформацію:
#  Імена тих, хто отримав купон, але не скористався,
# також вивести їх кількість
#  Імена шахраїв, які скористались знижкою, але магазин
# не давав їм купони

# def analyze_coupons(received_coupons,used_coupons):
#
#     received_coupons = set(received_coupons)
#     used_coupons = set(used_coupons)
#
#     unused_names = received_coupons - used_coupons
#     unused_count = len(unused_names)
#     fraud_names = used_coupons - received_coupons
#
#     return unused_count,unused_names,fraud_names
