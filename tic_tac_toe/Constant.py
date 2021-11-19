import datetime

SYMBOLS = ("X", "O")

COMP_RANDOM = [
    "LUFY",
    "NARUTO",
    "ICHIGO",
    "ASTA",
] # список случайных имён компьютера

PATTEREN_USER =(
    ("name", lambda *args, **kwargs: input("Введите ваше имя:")),# просим ввести имя
    ("symbol", lambda symbol, *args, **kwargs: symbol),# инициализируем символ
    ("steps", lambda *args, **kwargs: list()),# записывает в список все шаги
    ("all_steps", lambda *args, **kwargs: set()),#записываем все шаги всех пользователей
    ("user_type", lambda user_type, *args, **kwargs: user_type),# создана для понимания, комп это или человек
)

FILE_HANDLERS = {
    "GAME_NUM":  "game_num_inc",
    "INIT_GAME": "game_init",
    "GAME_STEP": "game_log",
}# названия фалов

INIT_ROW_TEMPLATE = {
    "game_id": int,
    "mode": str,
    "x_user_name": str,
    "o_user_name": str,
    "date_start": datetime.datetime.fromisoformat,
}