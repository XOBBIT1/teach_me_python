def same(*args, **kwargs):
    print(args)
    print(kwargs)
    pass

some_list = [1, 2, 3, 4, 5]

some_dtc = {
    "a": "aaa",
    "b": "bbb",
    "c": "ccc"
}

reslut = same(1, some_list, some_dtc, hello = 22)
print(reslut)

"""
(1, [1, 2, 3, 4, 5], {
    "a": "aaa",
    "b": "bbb",
    "c": "ccc"
} )

{
    "hello": 22
}
"""










"""

(1, [1, 2, 3, 4, 5])
{
    "a": "aaa",
    "b": "bbb",
    "c": "ccc",
    "hello": 22
}

"""

""" 
([1, 2, 3, 4, 5], )
{
"hello":  {"a": "aaa",
          "b": "bbb",
          "c": "ccc"}
 }
"""


"""
(1, 2, 3, 4, 5 )
{
    "a": "aaa",
    "b": "bbb",
    "c": "ccc"
}
"""

"""
("a", "b", "c")
{

}

"""

"""
( )
{
    "a" : 1, 
    "b" : 2
}
"""

"""

(1, 2, 3)

{
    "a": "aaa",
    "b": "bbb",
    "c": "ccc"
}

"""













user = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10 ]
b = set(uesr)
print(user[0])


"""

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

"""