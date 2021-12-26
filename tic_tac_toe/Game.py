from itertools import cycle
from Steps import step_from_user
from user import METHODS
from board import match_matrix, creat_board, board_print
from Constant import SYMBOLS
from game_logger import get_num_game,write_init, write_step

def game(users: list[dict, ...], board: list[list], mode, game_num): # на вход запрашивает пользователя, который является списком внутри которого словарь, а также доску(список списков )
    steps = set()# добавляем счётчик шагов
    for num_step, user in enumerate(cycle(users), 1): # формируем цикл с пронумерованным цикличным пользователем
        user["all_steps"] = steps
        print(f"Ход Игрока: {user['name']}") # выводим чей ход
        board_print(board)
        step = step_from_user(user, board) # применяем функцию step_from_user к пользователю и доске
        user["steps"].append(step)
        steps.add(step)
        write_step(user, step, num_step, game_num)
        if match_matrix(board): # матчим доску
            print(f"Победил: {user['name']}.")
            break # останваливаем игру
        if num_step > 8: # так же, если колличество занятых клеток буедт равно 8 или выше
            print("Ничья") # выводим ничью
            break # останавливаем игру
    print("GAME OVER")# выводим конец игры

def game_start() -> dict:# ничего не запрашиваем на вход
    print("Добро пожаловать в Х/O") # Выводим приветствие
    vars = ("Y", "N")  # Даём варианты ответ
    while True:  # Если истина
        user_input = input(f"Хотите ли ознакомится с правилами? {'/'.join(vars)} :")  # то справшиваем Реванш?
        if user_input == "RULES":
            print("Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики)."
                  "Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает."
                  "Первый ход делает игрок, ставящий крестики.Обычно по завершении партии выигравшая сторона зачёркивает чертой свои три знака (нолика или крестика), составляющих сплошной ряд")
            break
        else:
            print("Начнём игру")
            break
    game_num = get_num_game()
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
    init_data = {
        "users": users,
        "board": creat_board(3),#формируем размер доски
        "game_num": game_num,
        "mode": user_method
    }
    write_init(init_data)
    return init_data  # возвращаем доску, пользователя

def end_game( ):
    vars = ("Y", "N") # Даём варианты ответ
    while True: # Если истина
        user_input = input(f"Реванш? {'/'.join(vars)} ") # то справшиваем Реванш?
        if user_input == "N":
            print("Досвидания. Хоршего дня)")
            break
        elif user_input in vars: # проверям, что введённок пользователем находится в вариантах
            return user_input == vars[0] # если нет
        print("Неверный вывод, повторите ") # то цикл проходит снова


