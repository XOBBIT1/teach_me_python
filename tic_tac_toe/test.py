from Game import match_matrix
from Game import game, creat_board
from user import get_user
from Game import game_start
def test_board():
    matrix_test = (
        (([1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]), True),

        (([0, 1, 2],
          [0, 0, 1],
          [1, 1, 2]), False),

        (([1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]), True),

        (([0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]), True),

        (([0, 0, 2],
          [0, 0, 2],
          [0, 0, 2]), True),

        (([2, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), False),

        (([1, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), True),

        (([2, 1, 1],
          [0, 1, 2],
          [1, 0, 1]), True),
    )

    for test in matrix_test:
        assert match_matrix(test[0]) is test[1], test[0]

test_board()

game([{"name": 1, "token": "x"},{"name": 2, "token": "O"}], creat_board(3))

us = get_user("COMP","X")
print(us)

game_st = game_start()
print(game_st)