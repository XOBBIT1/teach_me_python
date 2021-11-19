import random # импортиреует random
from Constant import COMP_RANDOM, PATTEREN_USER


def comp(symbol)-> dict:#
    return { "name": random.choice(COMP_RANDOM), # Возвращает случайное имя компьютера
             "symbol": symbol, # символ нолик по дефолту становится символом компьютера
             "steps": [], # записивыет шаги компьютера в списке
             "all_steps": set(),
             "user_type": "COMP",
             }

def user(symbol)-> dict: # создаём пользователя, где пользователь словарь
    user = {}# пользователь словарь
    for i in PATTEREN_USER:# создаём цикл, который итерируется по  user_pattern
        user[i[0]] = i[1](symbol=symbol, user_type="USER")# 0 элемент кортежа в словаре, будет равен 1 элемнту кортежа, который находится в user_pattern
    return user #будет возвращаться, то что написал пользователь

METHODS= {
    "COMP": {"creator": comp}, # кулюч комп будет выводить значение функции comp, а то есть рандомного компьтера
    "USER": {"creator": user} # ключюзер выводе значение функции user
}

def get_user(m, symbol)-> dict:# является словарём
    return METHODS[m]["creator"](symbol=symbol)# возвращает выбор пользователя (COMP, USER)

