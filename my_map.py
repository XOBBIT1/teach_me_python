# Map
# Принемает функцию и Iterables
# В основном это цикл или кортеж
# Что он делает ? - Берёт любой итерируемы объект и применяет к нему функцию указанную пользователем.

def my_map(fanc, iterr):
        for n in iterr:
            while fanc(n):
                continue


def my_map1(fanc, iterr):
    for n in iterr:
        yield fanc(n)


i = [1, 2, 3, 4, 5]
a = my_map1(sum, i)
print(a)