"""
2. Задание
Даны данные человека
"""

name = "Василий"
surname = "Иванов"
age = 33
height = 182
year = 2021
birth_year = year - age
bio = name + " " + surname + " " + "ростом" + " " + str(height) + " " + "см"

print(birth_year, bio )

# вычислить Год рождения (относительно текущего года) и присвоить переменной birth_year
# Составить строку по шаблону {name} {surname} {birth_year} ростом {182} см и присвоить переменной bio
# Напечатать на экране значение bio
