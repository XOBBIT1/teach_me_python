"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user = str(input("Введите строку:\n"))
user_target = user.split(' ')
n = 0
while n < len(user_target):
     if len(user_target[n]) >= 10:
        print(f"{n+1}:{user_target[n][:10]} \n")
     else:
        print(f"{n + 1}:{user_target[n]} \n")
     n += 1
