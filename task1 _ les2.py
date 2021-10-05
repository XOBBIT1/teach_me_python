"""
1 Даны кортеж пользователей users и набор шаблонов templates
Задача обращаясь по индексу к кортежу пользователей напечатать на экране сообщение
если пользователю менее 7 лет: "{name} {surname} закончил школу"
Внимание конструкцию IF ELSE мы не используем (мы ее еще не изучали, и даже если знаете не используйте)
"""
dict_1 =  {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    }
dict_2  = {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }

users = (
    {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,
    },
    {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }
)

templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдет в школу",
)

