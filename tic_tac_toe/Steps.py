import random

def get_step() -> tuple:
    while True:
        res = [] # Добавляем список в который будем аппендить координаты пользователя
        step_user = input("Введите координаты хода через пробел \n") # Просим ввести координаты
        steps = step_user.split(" ") # Делаем из строки список и разбиваем по элементно, через пробел
        try:
            if len(steps) != 2: # Если длинна полученного списка не равна 2
                raise ValueError # товозбуждаем ошибку Значения
            for i in steps: # Формеруем цикл
                res.append(int(i)) # Который добавляет координаты в новый список
        except ValueError: # Если же число привишает 2
            print("Ошибка ввода. Повторите: ") # то перехватываем ValueError и пишем сообщение
            continue # продолжаем цикл
        return tuple(res) # возвращаем координаты

def chek_step(board: list[list], step: list[int, int] ):#  На вход принимает список списков и список индексов
    try:
        cell = board[step[0]][step[1]] # Смотрим, чтобы координаты не выходили за рамки
        if not cell: # если же ячейка пуста
            return True # то свободная
    except IndexError: #  если же IndexError
        print("Неверные координаты")# то пишем сообщение
    return False #  и возвращаем False


def step_from_user(user: dict, board: list[list]):
    if user["user_type"] == "COMP":
        step = step_auto(user, board)
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            return step
    while True: # Пока правда
        step = get_step() #  получаем координаты
        if chek_step(board, step): # если проверяем шаг
            board[step[0]][step[1]] = user["symbol"] # то передаём символ который закреплён за игроком
            return step# возвращает step
        else:
            print("Ячейка не существует или заята") # в ином случае, ячейка либо занята либо её нет
            continue # продолжаем провеку

def step_auto(user, board: list[list]):#
    board_size = len(board)# вычисляем длинну строки
    all_steps_variants = set((i, j) for i in range(board_size) for j in range(board_size))# формируем сет из набора кортежей всех ходов
    return random.choice(tuple(all_steps_variants.difference(user["all_steps"])))# возвращаем отличе от всех возможных ходов