from itertools import cycle
from Steps import step_from_user
from user import Methods, get_user
from Constant import SYMBOLS
from board import match_matrix, creat_board,board_print
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
    "Type": lambda pattern, **kwargs: pattern.format(variants = ("C","U") ),#будем хранить функции, которые будут возвращать готовую строку, учитывая данные, которые получит
    "Ask_step": lambda pattern, **kwargs: pattern.format(**kwargs),#будем хранить функции, которые будут возвращать готовую строку
    "Win":lambda pattern, **kwargs: pattern.format(**kwargs),#будем хранить функции, которые будут возвращать готовую строку
    "New_game": lambda pattern, **kwargs: pattern.format(variants = ("Y","N")),#будем хранить функции, которые будут возвращать готовую строку, учитывая данные, которые получит
    "Enter_name": lambda pattern, **kwargs: pattern.format(**kwargs)#будем хранить функции, которые будут возвращать готовую строку
}

pattern_user =(
    ("name",lambda *args,**kwargs:input("Введите ваше имя:")),# просим ввести имя
    ("symbol",lambda symbol, *args,**kwargs:symbol),# инициализируем символ
    ("steps",lambda *args,**kwargs: list()),# записывает в список все шаги
    ("all_steps",lambda *args, **kwargs: set()),#записываем все шаги всех пользователей
    ("user_type", lambda user_type, *args, **kwargs: user_type),# создана для понимания, комп это или человек
)
game_type = {
    "U": lambda x:" ",
    "C": lambda x:" "
}
def interface_user(pattern_name, **pattern_var):# на вход принемает один из ключей словаря pattern_variants, **pattern_var является **kwargs для универсальности
    if pattern_name in pattern_variants:# если pattern_name находится в pattern_variants
        ask_str = pattern_variants[pattern_name](inter_str[pattern_name], **pattern_var)#  так как ключом является lambda, то и на вход мы запрашиваем значения функции
        user_input = input(ask_str)# спрашиваем пользователя
        return user_input# возращаем ответ
    else:
        print(inter_str[pattern_name])# в ином случае просто выводим значение введённго ключа

def game(users: list[dict], board: list[list]):# на вход запрашивает пользователя, который является списком внутри которого словарь, а также доску(список списков )
    win_man = None
    num_step = 0
    steps = set()
    for num_step, user in enumerate(cycle(users)):# формируем цикл с пронумерованным цикличным пользователем
        user["all_steps"] = steps
        print(f"Ход Игрока: {user['name']}")# выводим чей ход
        board_print(board)
        step = step_from_user(user, board)# применяем функцию step_from_user к пользователю и доске
        user["steps"].append(step)
        steps.add(step)
        if match_matrix(board):# матчим доску
            win_man = user# если есть победитель, то запистываем в победители user
            break# останваливаем игру
        if num_step >= 8:# так же, если колличество занятых клеток буедт равно 8 или выше
            break# останавливаем игру
    return win_man, num_step

def game_start() -> dict:# ничего не запрашиваем на вход
    print("Добро пожаловать в Х/O") # Выводим приветствие
    user_method = {}# создаём словарь
    for idx, i in enumerate(Methods, 1):# формируем цикл
        user_method[idx] = i# элемент user_method, равен 1-ому элементу Methods
    method_s = "\n".join(f"{key}:{value}" for key,value in user_method.items())# формируем строку объединя через начало новой строки, формируем ключ\значение в user_method
    method_str = f"Выбериете номер режима игры\n{method_s}"# просим пользователя ввести число

    while True:# пока истина
        try:#пробуем
            method_input = int(input(method_str))# Ввод числа 1\2
            game_method = user_method[method_input]# присваиваем новой переменной значение словоря с номером
            break# останвливем опрос
        except ValueError:# Если же ошибка ввода по значению
            print("Надо ввести число!")# то выводим сообщение
        except KeyError:# Если же ошибка ключа
            print("Недопустимое значение")# то выводим сообщение
        continue# продолжаем
    users = []#форимруем переменную список
    for symbol, method in zip(SYMBOLS, ("USER", game_method)):# формируем цикл, где присваивется символ игроку
        user = get_user(method, symbol)# присваиваем переменной функцию
        users.append(user)# добовляем значение
    board = creat_board(3)#формируем размер доски
    return {
        "users": users,
        "board": board,
    } # возвращаем доску, пользователя


def end_game(num_step, winner):# на вход функция запрашивает, шаг и победителя
    res_srt = f"Победил {winner['name']}" if winner else "Ничья"# Пишем строку, если победитель, то выводим его имя, если нет, то Ничья
    print_res = f"На {num_step} ходу, { res_srt}"# Пишем на каком ходу
    print(print_res)# Выводим
    vars = ("Y", "N")# Даём варианты ответ
    while True:#Если истина
        user_input = input(f"Реванш? {'/'.join(vars)}")# то справшиваем Реванш?
        if user_input in vars:# проверям, что введённок пользователем находится в вариантах
            return user_input == vars[0]#если нет
        print("Неверный вывод, повторите ")#то цикл проходит снова
