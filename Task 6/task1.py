""" 1
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

user_list = user = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10 ]  # задаём список

def my_func(ell): # создаём функцию
    n = ell[0] # создаём переменную и присваиваем значение 0 элемената
    for elements in ell: # создаюм цикл в которм каждый элемент читается отдельно
        if elements > n: # проверяем, если предыдущий символ больше предыдущего
            yield elements # запускаем гениратор

for a in my_func(user_list): # если значение, есть в заданном списке
    print("Результат>>>", a) # то выводим его