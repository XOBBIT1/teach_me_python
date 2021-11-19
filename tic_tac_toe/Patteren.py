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
