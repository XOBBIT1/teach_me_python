import random # импортиреует random

COMP_RANDOM = [
    "LUFY",
    "NARUTO",
    "ICHIGO",
    "ASTA",
] # список случайных имён компьютера

user_pattern = (
    ("name", lambda *args,**kwargs: input("Введите ваше имя:")),# ввод имени пользователя
    ("symbol", lambda symbol, *args, **kwargs: symbol),# случайный символ пользователя
    ("steps", lambda *args, **kwargs: list()),# записивыет шаги пользователя в списке
)
def comp(symbol)-> dict:#
    return { "name" : random.choice(COMP_RANDOM), # Возвращает случайное имя компьютера
             "symbol": symbol, # символ нолик по дефолту становится символом компьютера
             "steps": [], # записивыет шаги компьютера в списке
             }

def user(symbol)-> dict: # создаём пользователя, где пользователь словарь
    user = {}# пользователь словарь
    for i in user_pattern:# создаём цикл, который итерируется по  user_pattern
        user[i[0]] = i[1](symbol=symbol)# 0 элемент кортежа в словаре, будет равен 1 элемнту кортежа, который находится в user_pattern
    return user #будет возвращаться, то что написал пользователь

Methods = {
    "COMP": {"creator": comp}, # кулюч комп будет выводить значение функции comp, а то есть рандомного компьтера
    "USER": {"creator": user} # ключюзер выводе значение функции user
}

def get_user(m, symbol)-> dict:# является словарём
    return Methods[m]["creator"](symbol=symbol)# возвращает выбор пользователя (COMP, USER)


us = get_user("COMP","X")
print(us)