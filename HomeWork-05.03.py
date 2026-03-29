# # Реалізуйте роботу банку. Усі дані зберігаються у
# # словнику, де ключ – ім’я клієнта, значення – баланс на
# # рахунку.
# # Напишіть функцію, яка отримує словник з даними та
# # зараховує гроші на баланс. Для цього вона запитує ім’я та
# # суму у користувача, якщо користувача немає, то вносить його
# # дані у словник, інакше додає суму до балансу.
#
#
# balances = {
#     "Дмитро": 2000,
#     "Олег": 5000,
#     "Марія": 11000,
# }
#
#
# def add_money_to_balance(balances_dict):
#     name = input("Введіть ім’я користувача: ")
#     amount = int(input("Введіть суму: "))
#
#     if name not in balances_dict:
#         balances_dict[name] = amount
#     elif name in balances_dict:
#         balances_dict[name] += amount
#
#     return balances_dict
#
#
# def withdraw_money(balances_dict):
#     name = input("Введіть ім’я користувача: ")
#     amount = int(input("Введіть суму: "))
#
#     if name not in balances_dict:
#         raise ValueError(" такого імені не існує")
#     elif balances_dict[name] < amount:
#         raise ValueError("на балансі недостатньо коштів")
#     else:
#         balances_dict[name] = balances_dict[name] - amount
#
#     return balances_dict
#
# def main():
#     print("1: поповнити рахунок")
#     print("2: зняти кошти")
#     print("3: завершити роботу")
#
#     while True:
#         choice = input("Введіть ваш вибір: ")
#
#         if choice == "3":
#             print("Дякуємо за використання програми!")
#             break
#         elif choice == "1":
#             print(add_money_to_balance(balances))
#         elif choice == "2":
#             try:
#                 withdraw = withdraw_money(balances)
#                 print("Ваш баланс", withdraw)
#             except ValueError as err:
#                 print("Помилка", err)
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")
#
#
# if __name__ == "__main__":
#     main()
