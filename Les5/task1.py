""" 1
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Результатом работы функции должна быть строка
Пример строки результата:
Иванов Иван Иванович 1986 года Рождения, проживающий в городе Норильск.
Контактные данные:
- телефон: 89181111111
- email: test@test.ru
"""


name = input('Введите ваше имя: ')
sername = input('Введите вашу фамилию: ')
year = int(input('Введите год вашего рождения: '))
city = input('Введите город проживания: ')
email = input('Введите ваш адрес эл. почты: ')
nomber = input('Введите ваш номер телефона: ')
def Data_user (name, sername, year, city, email, nomber):
     return name, sername, year, city, email, nomber
print(f"Name>>> {name}; \nSername>>> {sername}; \nBerth>>> {year};City>>> {city}; \nEmail>>> {email}; \nYour number>>> {nomber}")





