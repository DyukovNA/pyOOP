import doctest


class Cat:
    def __init__(self, name: str, hunger: int):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param name: Имя
        :param hunger: Голод от 0 до 100

        Примеры:
        >>> cat = Cat("Dog", 5)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if len(name) < 1:
            raise ValueError("Имя не может быть пустой строкой")
        self.name = name

        if not isinstance(hunger, int):
            raise TypeError("Голод должен быть типа int или float")
        if hunger < 0 | hunger > 100:
            raise ValueError("Голод должен быть числом от 0 до 100")
        self.hunger = hunger

    def pet(self) -> bool:
        """
        Функция которая позволяет погладить кота за счёт его голода

        :return: Смогли ли вы погладить кота

        Примеры:
        >>> cat = Cat("Dog", 55)
        >>> cat.pet()
        True
        """
        if self.hunger >= 50:
            return True
            print("Вы погладили кота")
            self.hunger -= 25
        else:
            return False
            print("Кот слишком голодный. Покормите его, чтобы его погладить")

    def feed(self, amount: int) -> None:
        """
        Функция котороя позволяет кормить кота

        :param: amount Количество корма

        :raise ValueError: Если количество корма больше, чем кот может съесть, то вызываем ошибку
        Примеры:
        >>> cat = Cat("Dog", 5)
        >>> cat.feed(75)
        """
        if not isinstance(amount, int):
            raise TypeError("Корм должен быть типа int или float")
        if amount <= 0 | amount > 100:
            raise ValueError("Корм должен быть числом от 1 до 100")
        if 100 < self.hunger + amount:
            raise ValueError("Корма слишком много, коту столько не съесть")
        self.hunger += amount

    def getHunger(self) -> int:
        """
        Функция которая позволяет узнать количество голода у кота

        :return: Количество голода у кота

        Примеры:
        >>> cat = Cat("Dog", 5)
        >>> cat.getHunger()
        5
        """
        return self.hunger


if __name__ == "__main__":
    doctest.testmod()
