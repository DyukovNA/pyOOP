import doctest


class Door:
    def __init__(self, height: (int, float), width: (int, float), state: bool):
        """
        Создание и подготовка объекта "Дверь"

        :param height: Высота
        :param width: Ширина
        :param state: Состояние, где False - открыта True - закрыта

        Примеры:
        >>> door = Door(200, 100, False)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int, float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int, float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(state, bool):
            raise TypeError("Состояние должно быть типа bool")
        self.state = state

    def open(self) -> None:
        """
        Функция которая позволяет открыть дверь

        :return: Вы открыли дверь

        Примеры:
        >>> door = Door(200, 100, False)
        >>> door.open()
        Вы открыли дверь
        """
        self.state = False
        print("Вы открыли дверь")

    def close(self):
        """
        Функция которая позволяет закрыть дверь

        Примеры:
        >>> door = Door(200, 100, False)
        >>> door.close()
        Вы закрыли дверь
        """
        self.state = True
        print("Вы закрыли дверь")

    def getPerimeter(self) -> (int, float):
        """
        Функция которая позволяет узнать периметр двери

        Примеры:
        >>> door = Door(200, 100, False)
        >>> door.getPerimeter()
        600
        """
        print(2 * (self.height + self.width))

if __name__ == "__main__":
    doctest.testmod()