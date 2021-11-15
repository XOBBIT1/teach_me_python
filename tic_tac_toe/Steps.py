def get_step() -> list [int,int]:
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
        return res # возвращаем координаты

def chek_step(board: list[list], step: list[int, int] ):#  На вход принимает список списков и список индексов
    try:
        cell = board[step[0]][step[1]] # Смотрим, чтобы координаты не выходили за рамки
        if not cell: # если же ячейка пуста
            return True # то свободная
    except IndexError: #  если же IndexError
        print("Неверные координаты")# то пишем сообщение
    return False #  и возвращаем False


def step_from_user(user: dict, board: list[list]):
    while True: # Пока правда
        step = get_step() #  получаем координаты
        if chek_step(board, step): # если проверяем шаг
            board[step[0]][step[1]] = user["token"] # то передаём символ который закреплён за игроком
            break # ломаем, чтобы прописалася, только один символ
        else:
            print("Ячейка не существует или заята") # в ином случае, ячейка либо занята либо её нет
            continue # продолжаем провеку