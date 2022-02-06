# Задание с корзиной
# some_dict = {'cheese': [10, 20], 'chicken': [15, 25], 'beef': [20, 10]}
# cart = {'cheese': 0, 'chicken': 0, 'beef': 0}
# print('Список продукции:', '\n Название: cheese - Цена:', some_dict['cheese'][0], '- Количество:',
#       some_dict['cheese'][1], '\n Название: chicken - Цена:', some_dict['chicken'][0], '- Количество:',
#       some_dict['chicken'][1], '\n Название: beef - Цена:', some_dict['beef'][0], '- Количество:', some_dict['beef'][1])
# choose = input('Введите название покупки:')
# choose_2 = int(input('Введите её количество:'))
# while choose != 'n':
#     if choose in some_dict:
#         if choose_2 <= some_dict[choose][1]:
#             cart[choose] += choose_2
#             c = some_dict[choose][1] - choose_2
#             some_dict[choose][1] = c
#         else:
#             print('Не хватает количества товара')
#             break
#         print('Название:', choose, '- Цена:', some_dict[choose][0], '- Количество:', some_dict[choose][1])
#     else:
#         print('Такого товара нет')
#     choose = input('Введите новое название:')
#     choose_2 = int(input('Введите количество:'))
# coast_all = (cart['cheese'] * 10) + (cart['chicken'] * 15) + (cart['beef'] * 20)
# print('Общая стоимость:', coast_all)
# print('Остатки продукции:', '\n cheese', some_dict['cheese'][1], '\n chicken', some_dict['chicken'][1], '\n beef',
#       some_dict['beef'][1])
