# №1
# matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 0],
#           [1, 3, 5, 7, 9],
#           [2, 4, 6, 8, 0],
#           [1, 4, 7, 0, 3]]
# count = []
# for i in matrix:
#     a = sum(i)
#     count.append(a)
# print(count)
# print(count.index(max(count)))
# №2
# while True:
#     try:
#         nums = input('Введите числа через пробел:')
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
