def match_matrix(board):# на вход принемаем доску
    def chel_line(line):# внутри функци создаём ещё одну, на проверку линий
        line_set = set(line)# убираум повторения в линиях
        if (0 not in line_set and len(line_set) == 1):# если размер доски равен 0, то победителя нет, если же 1, то уже имеется победитель
            return True# возвращаем истину
        else:
            return False# в противном случаи ложь
    diagonal = map(lambda idx: board[idx][idx], range(0, len(board)))# формируем диагонали(lambda на вход принимает знаение all_board в нутри которй row поиндексно (0:0))
    diagonal_revers = map(lambda idx: board[idx][len(board) - idx - 1], range(len(board) -1, -1, -1))# тоже самое но теперь с другой диагональю
    pre_res = any(map(chel_line, (diagonal,diagonal_revers)))# матчим диагонали
    if pre_res:#  если же хоть одна из них сформирована
        return True# то возвращаем истину
    for r, c in zip(board, zip(*board)):# ЕСТЬ ВОПРОС
        pre_res = any(map(chel_line,(r,c)))# колонки, и строки матчатся
        if pre_res:# если же сформирован, хоть 1 из вариантов
            return True# то возвращаем истину
    return False# возвращаем ложь

def creat_board(size): # на вход запрашиваем размер
    all_board = [] # формируем список
    for i in range(size):# формируем цикл с размерностью size
        row = []# внутри all_board формеруем ещё один список
        for i in range(size):# формируем цикл с размерностью size, но уже в row
            row.append(0)# добавляем 0 в список
        all_board.append(row)# так же добавляем списко в список
    return all_board# возвращам 1-ый список

def board_print(board):# на вход запрашивает доску
    title_row = f'##{"#".join(map(str, range(len(board))))}#'# по длинне доски выстраиваем цифры
    row_str = "\n".join(map(lambda i: f"{i[0]}#{'|'.join(map(str,i[1]))}#",enumerate(board)))# берём каждую строку инумеруюем через кортеж списки, но так как join работает только со строками, то конвертируем в строку
    print(f"{title_row}\n{row_str}\n{'#'* len(title_row)}")# выводим строки и закрываем # по всей длинне строк(нижняя линия)
