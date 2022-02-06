# Задания из презетации
# №1
# nums = [1, 5, 6, 3, 2, 1, 7, 1, 2, 3, 0, 4]
# nums_2 = set(nums)
# print(len(nums) == len(nums_2))
# №2
# nums = {'one': 1, 'two': 2, 'three': 3}
# nums['four'] = 4
# print(nums)
# nums[('sometuple', 'sometuple_2')] = ['someshit', 'someshit2']
# print(nums)
# key = nums['two']
# print(key)
# delete = nums.pop('one')
# print(nums)
# print(nums.keys())
# №3
# nums = set([1, 2, 3, 4, 5, 6, 7])
# nums_2 = frozenset([1, 3, 5, 7, 9])
# print(nums | nums_2)
# print(nums & nums_2)
# Дз из конфы
# №1
# nums = {1, 2, 3, 4, 2, 3}
# print(len(nums))
# №2
# nums = {1, 2, 3, 4, 5}
# nums_2 = {1, 3, 5}
# print(len(nums & nums_2))
# №3
# nums = list(map(int, input('Введите числа через пробел:').split(' ')))
# nums_2 = set()
# for i in nums:
#     if i in nums_2:
#         print('Yes')
#     else:
#         print('NO')
#         nums_2.add(i)
# №4
# words = input('Введите буквы:')
# words_2 = set(words)
# print(len(words_2))
# №5
# a = {1, 3, 2}
# b = {4, 3, 2}
# c = a & b
# print(c)
# №6
# a = {1, 3, 2}
# b = {4, 3, 2}
# c = b - a
# print(c)
# №7
# words = input('Введите буквы:')
# words_2 = set(words)
# print('YES') if len(words_2) == 26 else print('NO')
# №8
# year = int(input('Введите числа:'))
# for y in range(year + 1, year * 2):
#     if len(set(str(y))) == 4:
#         print(y)
#         break
