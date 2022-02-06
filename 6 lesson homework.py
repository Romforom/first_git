# Задача №1
# list_1 = [15, 48, 'hello', 6, 19, 'world']
# glasnie = ['a', 'e', 'i', 'u', 'o']
# vowels = 0
# non_vowels = 0
# for i, item in enumerate(list_1[:]):
#     if isinstance(item, int):
#         if item % 2 == 0:
#             string_1 = str(item)
#             summa = sum(map(int, string_1))
#             print(summa)
#         else:
#             list_1[i] = 1
#     else:
#         count = 0
#         for letter in item:
#             if letter in glasnie:
#                 count += 1
#         vowels += count
#         non_vowels += len(item) - count
# print(list_1)
# print('Количество гласных: ', vowels)
# print('Количество согласных: ', non_vowels)

# Задача №2
# words = input('Введите через пробел список: ').split(' ')
# print(words[0])
# print(words[len(words) // 2])
# print(words[-1])

# Задача №3
# numbers = list(map(int, input('Введите через пробел список чисел: ').split(' ')))
# number = int(input('Введите число n: '))
# print(numbers[number] ** number)

# Задача №4
# numbers = list(map(int, input('Введите через пробел список чисел: ').split(' ')))
# numbers_2 = list(sorted(numbers, reverse=True))
# print(numbers)
# print(numbers_2)
# if numbers == numbers_2:
#     print('ДА')
# else:
#     print('НЕТ')

# numbers = list(map(int, input('Введите через пробел список чисел: ').split(' ')))
# numbers_2 = numbers[:]
# numbers_2.sort(reverse=True)
# if numbers == numbers_2:
#     print('Да')
# else:
#     print('Нет')

# Задача №5
# words_1 = input('Введите через пробел список: ').split(' ')
# words_2 = input('Введите через пробел список: ').split(' ')
# for word in words_1[:]:
#     if word in words_2:
#         print(word)
