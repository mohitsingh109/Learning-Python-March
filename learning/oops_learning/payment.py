from abc import ABC, abstractmethod
# from <filename> import <class, function, variable>

class PaymentMethod(ABC):
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def __init__(self, name, phone, upi_id):
        super().__init__(name, phone)
        self.__upi_id = upi_id

    def get_upi_id(self):
        return self.__upi_id

    def pay(self, amount):
        print(f"Paying {amount} using UPI with id {self.__upi_id}")

class CreditCard(PaymentMethod):
    def __init__(self, name, phone, credit_card_id):
        super().__init__(name, phone)
        self.__credit_card_id = credit_card_id

    def get_credit_card_id(self):
        return self.__credit_card_id

    def pay(self, amount):
        print(f"Paying {amount} using Credit Card with id {self.__credit_card_id}")


upi = UPI("Mohit", "243432", "khdhfs")
credit_card = CreditCard("Mohit", "243432", "kdskhsfvfd")

payments = [upi, credit_card]

for p in payments:
    p.pay(1000)