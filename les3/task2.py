"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

number = int(input("Введите числа:\n"))
if number <= 3:
    if number <= 1:
        print("Месяц:Январь\n"
              "Время года:Зима")
    if 1 < number <= 2:
        print("Месяц:Февраль\n"
              "Время года:Зима")
elif 3 < number <= 6:
    if number <= 3:
        print("Месяц:Март\n"
              "Время года:Весна")
    if 3 < number <= 4:
        print("Месяц:Апрель\n"
              "Время года:Весна")
    if 4 < number <= 5:
        print("Месяц:Май\n"
              "Время года:Весна")
elif 6 < number <= 9:
    if number <= 6:
        print("Месяц:Июнь\n"
              "Время года:Лето")
    if 6 < number <= 7:
        print("Месяц:Июль\n"
              "Время года:Лето")
    if 7 < number <= 8:
        print("Месяц:Август\n"
              "Время года:Лето")
elif 9 < number <= 12:
    if number <= 9:
        print("Месяц:Сентябрь\n"
              "Время года:Осень")
    if 9 < number <= 10:
        print("Месяц:Октябрь\n"
              "Время года:Осень")
    if 10 < number <= 11:
        print("Месяц:Ноябрь\n"
              "Время года:Осень")
    if 11 < number <= 12:
        print("Месяц:Декабрь\n"
              "Время года:Зима")
else:
    print("Нет такого месяца")