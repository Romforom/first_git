# задание 1
# num_1 = 17 / 2 * 3 + 2
# num_2 = 2 + 17 / 2 * 3
# num_3 = 19 % 4 + 15 / 2 * 3
# num_4 = (15 + 6) - 10 * 4
# num_5 = 17 / 2 % 2 * 3 ** 3
# print(num_1, num_2, num_3, num_4, num_5)

# Задание 2
# num_1 = 17 / 2 * (3 + 2)
# num_2 = (2 + 17) / 2 * 3
# num_3 = 19 % (4 + 15) / 2 * 3
# num_4 = ((15 + 6) - 10) * 4
# num_5 = 17 / 2 % (2 * 3) ** 3
# print(num_1, num_2, num_3, num_4, num_5)

# задание 3
# money = 11
# coast = 1.5
# bread = 3
# short_change = money - bread * coast
# print('У Анны осталось:', short_change, 'рублей')

# Задание 4
# Name = bool(input('Введите имя:'))
# print(Name)

# Задание 5
# apple_1 = 2
# apple_2 = 5
# print('У Пола ', apple_2, 'яблок. У Анны ', apple_1, 'яблок.')

# Задание 6
# L = int(input('Введите длину ребра куба:'))
# L = 4
# S = L ** 2
# V = L ** 3
# print('Длина ребра куба:', L, 'Площадь боковой поверхности куба:', S, 'Объём куба:', V)

# Задание 7
# import random as r
# num = r.randint(100, 1000)
# list_1 = [int(num_new) for num_new in str(num)]
# print(num)
# print(list_1)
# print(sum(list_1))
# Вариант 2
# import random as r
# num = r.randint(100, 1000)
# num2 = str(num)
# num3 = map(int, num2)
# print(num)
# print(sum(num3))

# print("\tВведите X1 и Y1:\n")
# X1 = float(input())
# Y1 = float(input())
# print("\tВведите X2 и Y2:\n")
# Y2 = float(input())
# X2 = float(input())
# k = (Y1 - Y2) / (X1 - X2)
# b = (Y2 - k * X2)
# print("X1 и Y1:", X1, Y1, "X2 и Y2:", X2, Y2)
# print("\ty = %.3f*x + %.3f" % (k,b))

# name1 = "Kate"
# name2 = "Roma"
# print(" %s, %s " %(name2, name1))

# num1 = int(input('Введите число 1:'))
# num2 = int(input('Введите число 2:'))
# num3 = int(input('Введите число 3:'))
# if num1 > num2 and num1 > num3:
#     print('Число 1 самое большое')
# elif num1 < num2 and num1 > num3:
#     print('Число 2 самое большое')
# else:
#     print('число 3 самое большое ')
