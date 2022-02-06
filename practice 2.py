# КР№1
# numbers = input('Введите 7 значное число:')
# count_1 = 0  # четные
# count_2 = 0  # нечётные
# nums = list(map(int, numbers))
# for i in nums:
#     if i % 2 == 0:
#         count_1 += 1
#     else:
#         count_2 += 1
# if count_1 > count_2:
#     print(sum(nums))
# else:
#     num = nums[0] * nums[2] * nums[5]
#     print(num)

# КР№2
# sentence = input('Введите текст:')
# glasnie = 'ауоиэыяюеё'
# punctuation = [' ', ',', '.', '!', '?']
# letters = []
# vowels = 0
# non_vowels = 0
# for letter in sentence[:]:
#     if letter not in punctuation:
#         if letter.lower() in glasnie:
#             letters.append(letter)
#             vowels += 1
#         else:
#             non_vowels += 1
# if vowels == non_vowels:
#     print(letters)
# print(vowels)
# print(non_vowels)

# КР№3
# import random
#
# number_1 = int(input('Введите число 1 от 1 до 20:'))
# number_2 = int(input('Введите число 2 от 1 до 20:'))
# number_3 = random.randint(1, 20)
# number_4 = random.randint(1, 20)
# arr_1 = []  # список для числа 3
# arr_2 = []  # список для числа 4
# count_1 = 0  # счётчик когда пара больше
# count_2 = 0  # всё остальное
# count_3 = 0
# while count_3 <= 7:
#     if number_1 > number_3 and number_2 > number_4:
#         count_1 += 1
#     else:
#         count_2 += 1
#     arr_1.append(number_3)
#     arr_2.append(number_4)
#     number_1 = int(input('Введите новое число 1 от 1 до 20:'))
#     number_2 = int(input('Введите новое число 2 от 1 до 20:'))
#     number_3 = random.randint(1, 20)
#     number_4 = random.randint(1, 20)
#     count_3 += 1
# if count_1 == count_2:
#     print(arr_1[3], arr_2[3])
# print(arr_1)
# print(arr_2)

# КР№ 4
# import random
#
# nums_1 = int(input('Введите количество выводимых случайных чисел:'))
# num = int(input('Введите искомую цифру:'))
# arr = []
# count = 0
# i = 1
# while i <= nums_1:
#     number_1 = random.randint(1, 100)
#     arr.append(number_1)
#     i += 1
# prepbignum = list(map(str, arr))
# bignum = ''.join(prepbignum)
# for number in map(int, bignum):
#     if number == num:
#         count += 1
# print(arr)
# print(bignum)
# print(count)

# КР№5
# sentence = input('Введите предложение включающее числа и знаки перпинания:')
# words = sentence.split(' ')
# numbers = [''.join(filter(lambda x: x.isdigit(), word)) for word in words]
# print(*list(filter(None, numbers)))

# КР№6
# word = input('Введите слово:')
# glasnie = 'ауоиэыяюеё'
# count_1 = 0  # пары верхнего регистра
# count_2 = 0  # пары нижнего регистра
# vowels = 0  # гласные
# for idx, i in enumerate(word[:-1]):
#     if i.isupper() and word[idx + 1].isupper():
#         count_1 += 1
#     if i.islower() and word[idx + 1].islower():
#         count_2 += 1
# for letter in word:
#     if letter.lower() in glasnie:
#         vowels += 1
# non_vowels = len(word) - vowels
# print('Пар верхего регистра', count_1)
# print('Пар нижнего регистра', count_2)
# print('Гласных', vowels)
# print('Согласных', non_vowels)
# print('Букв в слове', len(word))
