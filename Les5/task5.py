"""5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ (например Q), выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def my_func ():
    sum_res = 0
    out = False
    while out == False:
        item = input('введите числа через пробел или s - для выхода ').split()
        res = 0
        for element in range(len(item)):
            if item[element] == 's':
                ext = True
                break
            else:
                res = res + int(item[element])
        sum_res = sum_res + res
        print(f'сумма = {sum_res}')
    print(f'общая сумма = {sum_res}')
my_func()



