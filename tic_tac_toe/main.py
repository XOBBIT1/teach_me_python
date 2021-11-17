from board import creat_board
from Game import game_start, end_game, game

def main():# ничего не принемает
    game_vars = game_start() # инициализирует игру
    end_res = True# ставим, что end_res является истина
    while end_res:# начало уикла игры
        res_game = game(**game_vars)# ожидаем результата игры
        end_res = end_game(*res_game)# получив результат мы передаём его в end_game
        if end_res:# если end_res истина
            game_vars["board"] = creat_board(3)# то генерируем доску занова


if __name__ == '__main__':
    main()