# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата карткою {amount}  {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата PayPal {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата криптогаманцем {amount} {self.currency}")


def create_payment():
    payment_type = input("Введіть тип (card/paypal/crypto): ")
    currency = input("Введіть валюту: ")

    if payment_type == "card":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Невідомий тип")
        return None


payments = []

for _ in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)


for payment in payments:
    payment.pay(100)
