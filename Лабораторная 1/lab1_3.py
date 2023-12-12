import doctest


class HardDiskDrive:
    def __init__(self, brandName: str, storage: (int, float)):
        """
        Создание и подготовка к работе объекта HardDiskDrive

        :param brandName: Название производителя
        :param storage: Место на диске

        Примеры:
        >>> hdd = HardDiskDrive("Samsung", 1000000)
        """
        if not isinstance(brandName, str):
            raise TypeError("Имя должно быть типа str")
        if len(brandName) <= 0:
            raise ValueError("Имя не может быть пустой строкой")
        self.brandName = brandName

        if not isinstance(storage, (int, float)):
            raise TypeError("Место должно быть типа int, float")
        if storage <= 0:
            raise ValueError("Место должно быть положительным числом")
        self.storage = storage

    def addData(self, storage: (int, float), amount: int) -> None:
        """
        Функция которая позволяет добавить данные на диск

        :param storage: Объём одного файла
        :param amount: Количество файов

        Примеры:
        >>> hdd = HardDiskDrive("Samsung", 1000000)
        >>> hdd.addData(123456.7, 3)
        """
        if not isinstance(storage, (int, float)):
            raise TypeError("Место должно быть типа int, float")
        if storage <= 0:
            raise ValueError("Место должно быть положительным числом")

        if not isinstance(amount, int):
            raise TypeError("Количество должно быть типа int, float")

        if self.storage < storage * amount:
            raise ValueError()
        self.storage -= storage * amount

    def calcAmount(self, storage: (int, float)) -> int:
        """
        Функция которая позволяет рассчитать сколько файлов данного размера поместится на диск

        :param storage: Объём одного файла

        >>> hdd = HardDiskDrive("Samsung", 1000000)
        >>> hdd.calcAmount(23456.1)
        42
        """
        if not isinstance(storage, (int, float)):
            raise TypeError("Место должно быть типа int, float")
        if storage <= 0:
            raise ValueError("Место должно быть положительным числом")

        return int(self.storage // storage)

if __name__ == "__main__":
    doctest.testmod()