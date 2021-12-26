inter_str = {
    "HElP": "HElP",
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