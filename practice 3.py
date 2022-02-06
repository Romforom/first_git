# №1
# rick = ['never', 'gonna', 'give', 'you', 'up', 'never', 'gonna', 'let', 'you', 'down']
# c = []
# for i in rick:
#     if rick.count(i) < 2:
#         c.append(i)
# print(c)
# №2
# from math import floor
#
# numbers = [1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 3]
# c = 0
# for n in set(numbers):
#     if numbers.count(n) >= 2:
#         c += floor(numbers.count(n) / 2)
# print(c)
# №3
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# print('Сумма больше в кортеже С_1') if sum(C_1) > sum(C_2) else print('Сумма больше в кортеже 2')
# print('Кортеж С_1 \nМинимальное значение под индексом:', C_1.index(min(C_1)), '\nМаксимальное значение под индексом:',
#       C_1.index(max(C_1)))
# print('Кортеж С_2 \nМинимальное значение под индексом:', C_2.index(min(C_2)), '\nМаксимальное значение под индексом:',
#       C_2.index(max(C_2)))
# №4
# word = 'An apple a day keeps the doctor away'
# letter_list = []
# num_list = []
# set_word = set(word.lower())
# for l in set_word:
#     letter_list.append(l)
#     num_list.append(word.lower().count(l))
# d = dict(zip(letter_list, num_list))
# print(d)
# №5
# market = {'торт': {'состав': 'мука, кефир, сахар, яйца, какао', 'цена': 30, 'количество': 2000},
#           'пирожное': {'состав': 'печенье, сгущёное молоко, сливочное масло, какао, ликёр', 'цена': 20,
#                        'количество': 2000},
#           'маффин': {'состав': 'мука, молоко, сахар, яйца, сливочное масло, разрыхлитель', 'цена': 10,
#                      'количество': 2000}}
# cart = {'торт': 0, 'пирожное': 0, 'маффин': 0}
# print('Введите:\n'
#       'Если хотите посмотреть состав: название – состав\n'
#       'Если хотите посмотреть цену: название – цена\n'
#       'Если хотите посмотреть количество: название – количество\n'
#       'Вся информация: информация\n'
#       'Приступить к покупке: купить\n'
#       'Выйти: выйти\n')
# choose = input('Ввод:')
# while choose != 'выйти':
#     if choose in market:
#         choose_2 = input('Ввод:')
#         if choose_2 in market[choose]:
#             print(market[choose][choose_2])
#     if choose == 'информация':
#         print(market)
#     if choose == 'купить':
#         while choose != 'выйти':
#             choose = input('Введите что вы хотите купить, для выхода введите "выйти":')
#             if choose in market:
#                 weight = int(input('Введите вес в граммах:'))
#                 if weight <= market[choose]['количество']:
#                     cart[choose] += weight
#                     market[choose]['количество'] -= weight
#                 else:
#                     print('Не хватает количества товара')
#                     break
#     print('Полная стоимость:', (cart['торт'] / 100) * 30 + (cart['маффин'] / 100) * 10 + (cart['пирожное'] / 100) * 20)
#     print('Остаток:\nторт', market['торт']['количество'], '\nпирожное', market['пирожное']['количество'], '\nмаффин',
#           market['маффин']['количество'])
#     choose = input('Ввод:')
# №6
# nums_1 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
# nums_2 = [3, 6, 9, 2, 0, 12, 23, 17]
# count = 0
# for i in nums_1:
#     for j in nums_2:
#         if i == j:
#             count += 1
# print(count)
# №7
# while True:
#     try:
#         nums = input('Введите два числа через пробел:')
#         new_nums = nums.split(' ')
#         new_nums_1 = list(map(int, new_nums))
#         print(new_nums_1)
#         answer = new_nums_1[0] / new_nums_1[1]
#         print(answer)
#     except ValueError:
#         print('Были введены не числа')
#     except ZeroDivisionError:
#         print('Нельзя делить на 0')
#     else:
#         print('Ответ:', answer)
#         break
#     finally:
#         print('YESYESYES!')
# №8
# with open('text.txt', 'r') as f:
#     d = {l.rsplit(' ', 1)[0]: int(l.rsplit(' ', 1)[1]) for l in f}
# for name, mark in d.items():
#     if mark <= 3:
#         print(name)
# print('Средний балл по классу:', sum(d.values()) / len(d.values()))
