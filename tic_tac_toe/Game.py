from itertools import cycle
from  Steps import step_from_user


"""
Крестики нолики
"""
"""
Правила игры
1. Игровое поле 3х3 
2. 2-а игрока или компъютер
3. Игроки ходят поочереди
4. Победитель определяется, когда один
из игроков заполнит 3-и клетки(горизонтальная, вертикальная, наискосок)
5. Может быть ничъя 
"""
# TODO: Играть с компьютером
# TODO: Игровое поле в виде матрици 3х3 не изменяемо
# TODO: Ячейка игрового поля будет изменяться,
"""(
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
)
"""
# TODO: Игрок - Словарь
# TODO: Управляющий игрой распорядитель
# TODO: Функция матчинга игрового поля на наличие победителя
# TODO: Функция определения возможности хода
# TODO: Функция Взамодействия с пользователем
# TODO: Функция совершение кода, Записывает в поле в ячейку самого пользователя


inter_str = {
    "Rules": "",
    "Hello": "Добро пожаловать в Крестики/нолики ",
    "Name": "Введите имя",
    "Mod": "С кем вы будете играть? {variants}",
    "Ask_step": "Ход #{step_number} грока {name}",
    "Win": "Победу одержал {name} на ходу {step_number}",
    "New_game":"Желаете насать новую игру ? {variants}",
    "Draw": "Ничья"
}

pattern_variants = {
    "Type": lambda pattern, **kwargs: pattern.format(variants = ("C","U") ), #будем хранить функции, которые юудут возвращать готовую строку, учитывая данные, которые получит
    "Ask_step": lambda pattern, **kwargs: pattern.format(**kwargs),
    "Win":lambda pattern, **kwargs: pattern.format(**kwargs),
    "New_game":lambda pattern, **kwargs: pattern.format(variants = ("Y","N")),#будем хранить функции, которые юудут возвращать готовую строку, учитывая данные, которые получит
    "Enter_name":lambda pattern, **kwargs: pattern.format(**kwargs)
}

game_type = {
    "U": lambda x:" ",
    "C": lambda x:" "
}
def interface_user(pattern_name, **pattern_var):
    if pattern_name in pattern_variants:
        ask_str = pattern_variants[pattern_name](inter_str[pattern_name], **pattern_var)
        user_input = input(ask_str)
        return user_input
    else:
        print(inter_str[pattern_name])

def creat_board(size):
    all_board = []
    for i in range(size):
        row = []
        for i in range(size):
            row.append(0)
        all_board.append(row)
    return all_board

def match_matrix(board):
    def chel_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            return True
        else:
            return False
    diagonal = map(lambda idx: board[idx][idx], range(0, len(board)))#возвращаем от доски индексы
    diagonal_revers = map(lambda idx: board[idx][len(board) - idx - 1], range(len(board) -1, -1, -1))
    pre_res = any(map(chel_line, (diagonal,diagonal_revers)))
    if pre_res:
        return True
    for r, c in zip(board, zip(*board)):# ЕСТЬ ВОПРОС
        pre_res = any(map(chel_line,(r,c)))
        if pre_res:
            return True
    return False


def game_start(users: list[dict], board: list[list]):
    for num_step, user in enumerate(cycle(users)):
        print(f"Ход Игрока: {user['name']}")
        step_from_user(user,board)
        if match_matrix(board):
            print(f"Победил {user['name']}")
            break
        if num_step >= 8:
            print("Ничья")
            break
    print("Game Over")



