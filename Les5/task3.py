"""3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func (a,d,z):
    if a > d and z > d:
        result = a + z
        return result
    elif z > a and d > a:
        result = z + d
        return result
    else:
       result = d + a
       return result

res = my_func(
    int(input("Введите первое число:")),
    int(input("Введите вторрое число:")),
    int(input("Введите третье  число:"))
)
print("Результат =", res)
