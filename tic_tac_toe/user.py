import random # импортиреует random
from Constant import COMP_RANDOM

user_pattern = (
    ("name", lambda *args,**kwargs: input("Введите ваше имя:")),# ввод имени пользователя
    ("symbol", lambda symbol, *args, **kwargs: symbol),# случайный символ пользователя
    ("steps", lambda *args, **kwargs: list()),# записивыет шаги пользователя в списке
)
def cr_comp(symbol)-> dict:#
    return {
        "name" : random.choice(COMP_RANDOM), # Возвращает случайное имя компьютера
        "symbol": symbol, # символ нолик по дефолту становится символом компьютера
        "steps": [], # записивыет шаги компьютера в списке
        "user_type": "COMP",
        "all steps": set(),
    }

def cr_user(symbol)-> dict: # создаём пользователя, где пользователь словарь
    user = {}# пользователь словарь
    for i in user_pattern:# создаём цикл, который итерируется по  user_pattern
        user[i[0]] = i[1](symbol=symbol, user_type="USER")# 0 элемент кортежа в словаре, будет равен 1 элемнту кортежа, который находится в user_pattern
    return user #будет возвращаться, то что написал пользователь

Methods = {
    "COMP": {"creator": cr_comp}, # кулюч комп будет выводить значение функции comp, а то есть рандомного компьтера
    "USER": {"creator": cr_user} # ключюзер выводе значение функции user
}

def get_user(m, symbol)-> dict:# является словарём
    return Methods[m]["creator"](symbol=symbol)# возвращает выбор пользователя (COMP, USER)


