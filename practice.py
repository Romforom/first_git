# №1
# n = int(input('Введите число по вертикали:'))
# m = int(input('Введите число по горизонтали:'))
# k = int(input('Введите число долек:'))
# if k < n * m and k % n == 0 or k % m == 0:
#     print("YES!YES!YES!")
# else:
#     print("NO!NO!NO!")

# №2
# import random
#
# number = 0
# count = 0
# while number <= 10:
#     number = random.randint(1, 10)
#     count += 1
#     print(number)
#     if number == 10:
#         print('Число 10 выпало с:', count, 'попытки.')
#         break

# №3
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# for num in range(a, b + 1):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0 and num % 5 != 0:
#         print('Fizz')
#     elif num % 3 != 0 and num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# №4
# word_1 = input('Введите первое слово: ')
# word_2 = input('Введите второе слово: ')
# while word_1[-1] == word_2[0]:
#     word_1 = word_2
#     word_2 = input('Введите новое слово: ')
# print(word_2)

# №5
# numbers_1 = [" ".join(map(str, range(10)))] * 9
# for line in numbers_1:
#     print(line)

# №6
# for i in range(10):
#     print(" ".join(str(i) * 9))

# №7 Ромб
# n = int(input('Введите размер ромба:'))
# w = n * 2 - 1
# ar = []
# for y in range(w):
#     ar.append([])
#     for x in range(w):
#         d = n - abs(x + 1 - n) - abs(y + 1 - n)
#         ar[y].append(f"{d} " if d > 0 else "  ")
# for l in ar:
#     print(*l, sep="")

# №8
# k = input('Введите список через запятую:').split(",")
# print(k)
# places = list(sorted(k, key=lambda x: int(x.split(" ")[1])))[:3]
# print(places)

# №9 C ним помогли немного, если есть более простой вариант без вылавливания ошибок я бы глянул
# randomwords = input('Введите случайную фразу:')
# print('Введите слова из фразы не повторяясь:')
# words = list(map(str.lower, iter(input, '')))
# randomwords = list(map(lambda x: x.strip(",!?."), randomwords.lower().split(" ")))
# result = "Да"
# try:
#     prev_idx = randomwords.index(words[0])
# except ValueError:
#     result = "Нет совпадений"
#     prev_idx = -1
# for word in words[1:]:
#     try:
#         idx = randomwords.index(word)
#     except ValueError as err:
#         result = "Нет совпадений"
#         break
#     if prev_idx > idx and prev_idx != -1:
#         result = "Нет"
#         break
#     prev_idx = idx
# print(result)

# №10
# numbers = []
# number = int(input('Введите число:'))
# while number != 0:
#     if number % 3 == 0 and number % 10 == 8:
#         numbers.append(number)
#     number = int(input('Введите новое число:'))
# print(sum(numbers))

# №11
# ar = list(range(5, 16))
# print(ar)

# №12
# ar = list(range(1, 11))
# ar_2 = []
# for i in ar[:-1]:
#     a = ar[i - 1] * ar[i]
#     ar_2.append(a)
# print(ar_2)

# №13
# table = []
# for i in range(1, 10):
#     table.append([])
#     for j in range(1, 10):
#         table[i - 1].append(i * j)
# print(table)

# №14
# sentеnce = input('Введите предложение:')
# new_sentence = ""
# sentence_1 = str.lower(sentеnce)
# for letter in sentence_1:
#     if letter <= 'и':
#         new_sentence += letter
# print(new_sentence)
