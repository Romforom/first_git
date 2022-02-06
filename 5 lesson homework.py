# Казино
# from random import randint
#
# number = randint(1, 10)
# color = randint(1, 2)
# for i in range(5):
#     a, b = list(map(int, input('Введите два числа через пробел: ').split(' ')))
#     if a == number and b == color:
#         print('Вы ввели верно')
#         break
#     else:
#         print('Вы не угадали')
# print('Правильный номер:', number, 'Правильный цвет: ', color)

# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов:
# «стоп»,«хватит», «достаточно» (маленькими буквами, без кавычек).
# Напишите программу, которая выводит количество введенных слов
# wordlist = []
# word = input('Введите слово: ')
# while word != 'стоп':
#     wordlist.append(word)
#     word = input('Введите новое слово: ')
# print(len(wordlist))

# Ещё так можно мне показали
# d = []
# for word in iter(input, 'stop'):
#     d.append(word)
# print(len(d))

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
# number = input('Введите число: ')
# if len(set(number)) == len(number):
#     print('Число не состоит из одинаковых цифр')
# elif len(set(number)) == 1:
#     print('Число состоит из одинаковых цифр')
# else:
#     if len(number) % len(set(number)) == 0:
#         print('Число состоит из нескольких повторяющихся цифр')
#     else:
#         print('Число состоит и из повторяющихся и из не повторяющихся цифр')

# Мастер Гервант
# prices = [25, 10, 5, 1]
# cost = int(input('Введите стоимость: '))
# coins = 0
# for price in prices:
#     while cost >= price:
#         cost -= price
#         coins += 1
# print('Количество монет:', coins)

# Банк
# Balance = int(input('Введите балланс на карте: '))
# cost = int(input('Введите стоимость покупки: '))
# product = 0
# while Balance > cost:
#     Balance -= cost
#     product += 1
#     cost = int(input('Введите стоимость новой покупки: '))
# print(product)
# print('Остаток на счёте:', Balance)

# Шеренги
# first, second, third, fourth = [], [], [], []
# count = 0
# for i in range(1, 21):
#     if count == 0:
#         first.append(i)
#         count += 1
#     elif count == 1:
#         second.append(i)
#         count += 1
#     elif count == 2:
#         third.append(i)
#         count += 1
#     elif count == 3:
#         fourth.append(i)
#         count = 0
# print(first, second, third, fourth)

# Ещё с шеренгами показали вот это
# d = []
# r = list(range(1, 21))
# for l in zip(*[iter(r)] * 4):
#     d.append(l)
# print(list(map(list, zip(*d))))
