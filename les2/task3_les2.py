"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""
numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []

even.extend(numbers)
odd.extend(numbers)

even.remove(44)
even.remove(22)
even.remove(54)
even.remove(912)
even.remove(18)
even.remove(76)
even.remove(654)
odd.remove(87)
odd.remove(345)
odd.remove(33)
odd.remove(11)
print(even, odd)