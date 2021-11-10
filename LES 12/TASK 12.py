class Board:

    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size):
        self.size = size
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()
        self._protected = 1111
        self.__private = 22222

    def print_board(self):
        pass

    def add_step(self, step: tuple[int, int]):
        pass

    def chek(self) -> bool:
        pass

    # Так как игры пока нет, то и сделать задание у меня не получается. Я не понимаю, как это сделать.#
    # К концу следующей недели будет готова рабо (надеюсь)#