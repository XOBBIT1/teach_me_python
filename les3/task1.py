"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

пример списка: [22, 11, 45, 87, 0, 1, 6]
результат работы алгоритма с данным списком: [11, 22, 87, 45, 1, 0, 6]

будьте внимательны, пользователь необзательно в качестве значений введет числа, преобразованием и проверками
заниматься не надо, только разделить то что ввел пользователь и получить список значений.
"""

user = input("Введите числа:\n")
number = user.split(' ')
n = 0
while n < len(number) - 1:
        number[n], number[n + 1] = number[n + 1], number[n]
        n += 2
        # if n(str) < len(number) - 1:
        #     print("Введите, пожалуйста, число")
print(number)