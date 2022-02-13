# объявление функции
# def a_function():
#     mass = [1, 3, 5, 8, 13, 42]
#
#     print(sum(mass))
#
#
# a_function()

# функция ретёрн
# def add(a, b):
#     return a - b
#
#
# a = add(5, 3)
# b = add(a=5, b=3)
# c = add(b=5, a=3)
# print(a, b, c)

# def add(a, b=2, c=3):
#     return a + b + c
#
#
# print(add(3))
# print(add(3, 5))
# print(add(1, 1, 2))
# print(add(c=4, a=1, b=2))

# args and kwargs
# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return (args, kwargs)
#
#
# print(many(1, 2, 3, name='Mike', job='Programmer'))

# global
# def function_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
#
#
# def function_b():
#     c = 3
#     return a + c
#
#
# print(function_a(), function_b())

# вложенные функции
# def func1(a, b):
#     def inner_func(x):
#         return x * x * x
#
#     return inner_func(a) + inner_func(b)
#
#
# print(func1(4, 5))

# №1
# def year_lip(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# print(year_lip(int(input('Введите год:'))))

# №2
# from math import sqrt
#
#
# def square(a):
#     P = a * 4
#     S = a * a
#     D = sqrt(a ** 2 + a ** 2)
#     return P, S, D, d
#
#
# print(square(float(input('Введите сторону квадрата:'))))

# №3
# def season(a):
#     if a == 12 or a <= 2:
#         print('winter')
#     elif a >= 3 and a <= 5:
#         print('spring')
#     elif a >= 6 and a <= 8:
#         print('summer')
#     elif a > 12:
#         print('Месяц выбран неверно')
#     else:
#         print('autumn')
#
#
# num = int(input('Введите месяц:'))
# season(num)

# №4
# def is_prime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return n == d
#
#
# n = int(input('Введите число:'))
# print(is_prime(n))

# №5
# from random import randint
#
# arr = []
# for i in range(10):
#     a = randint(1, 1000)
#     arr.append(a)
# print(arr)
#
#
# def average(arr):
#     return sum(arr) / len(arr)
#
#
# print(average(arr))
