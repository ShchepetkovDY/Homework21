from models.store_class import Store


class Shop(Store):
    """
    Класс магазина
    """

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def get_free_space(self, new_title):
        """
        Функция определения кол-ва свободного пространства в магазине
        """
        #Проверка на наличие свободных мест в магазине
        if self.get_unique_items_count() >= 5:
            if new_title not in self.items:
                raise Exception
        return super().get_free_space()

