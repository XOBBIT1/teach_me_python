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
