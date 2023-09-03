from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_count: int) -> None:
        """
        Магический метод инициализации объектов класса
        """
        super().__init__(name, price, quantity)
        self.sim_count = sim_count

    def __repr__(self) -> str:
        """
        Магический метод для текстового образа объекта класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_count})"

    @property
    def number_of_sim(self) -> int:
        """
        Получение количества сим-карт у объекта класса
        """
        return self.sim_count

    @number_of_sim.setter
    def number_of_sim(self, count: int):
        """
        Проверка, что количество сим-карт целое число >0
        """
        if count >= 0:
            self.sim_count = count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
