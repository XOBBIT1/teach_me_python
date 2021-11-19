from itertools import cycle
from Steps import step_from_user
from user import METHODS, PATTEREN_USER
from board import match_matrix, creat_board, board_print
from Constant import SYMBOLS

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


def interface_user(pattern_name, **pattern_var):# на вход принемает один из ключей словаря pattern_variants, **pattern_var является **kwargs для универсальности
    if pattern_name in pattern_variants:# если pattern_name находится в pattern_variants
        ask_str = pattern_variants[pattern_name](inter_str[pattern_name], **pattern_var)#  так как ключом является lambda, то и на вход мы запрашиваем значения функции
        user_input = input(ask_str)# спрашиваем пользователя
        return user_input# возращаем ответ
    else:
        print(inter_str[pattern_name])  # в ином случае просто выводим значение введённго ключа


def game(users: list[dict, ...], board: list[list], step_num): # на вход запрашивает пользователя, который является списком внутри которого словарь, а также доску(список списков )
    steps = set()# добавляем счётчик шагов
    for num_step, user in enumerate(cycle(users), 1): # формируем цикл с пронумерованным цикличным пользователем
        user["all_steps"] = steps
        print(f"Ход Игрока: {user['name']}") # выводим чей ход
        board_print(board)
        step = step_from_user(user, board) # применяем функцию step_from_user к пользователю и доске
        user["steps"].append(step)
        steps.add(step)
        if match_matrix(board): # матчим доску
            print(f"Победил: {user['name']}.")
            break # останваливаем игру
        if num_step > 8: # так же, если колличество занятых клеток буедт равно 8 или выше
            print("Ничья") # выводим ничью
            break # останавливаем игру
    print("GAME OVER")# выводим конец игры

def game_start() -> dict:# ничего не запрашиваем на вход
    print("Добро пожаловать в Х/O") # Выводим приветствие
    user_method = {}# создаём словарь
    for idx, i in enumerate(METHODS, 1):# формируем цикл
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
        user = METHODS[method]["creator"](symbol=symbol)# присваиваем переменной функцию
        users.append(user)# добовляем значение

    return {
        "users": users,
        "board": creat_board(3),#формируем размер доски
    } # возвращаем доску, пользователя

def end_game( ): # на вход функция запрашивает, шаг и победителя
    vars = ("Y", "N") # Даём варианты ответ
    while True: # Если истина
        user_input = input(f"Реванш? {'/'.join(vars)} ") # то справшиваем Реванш?
        if user_input == "N":
            print("Досвидания. Хоршего дня)")
            break
        elif user_input in vars: # проверям, что введённок пользователем находится в вариантах
            return user_input == vars[0] # если нет
        print("Неверный вывод, повторите ") # то цикл проходит снова


