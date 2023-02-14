
class Request:
    """
    Класс для обработки запроса, введенного пользователем
    """
    def __init__(self, string):
        decode_string = string.lower().split(" ")
        self.__from = decode_string[4]
        self.__to = decode_string[6]
        self.__amount = int(decode_string[1])
        self.__product = decode_string[2]


    @property
    def from_(self):
        return self.__from

    @property
    def to_(self):
        return self.__to

    @property
    def amount(self):
        return self.__amount

    @property
    def product(self):
        return self.__product

    def __repr__(self):
        return f"откуда - {self.from_} \nкуда - {self.to_} \nчто - {self.product} \nсколько - {self.amount}"
