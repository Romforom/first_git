import pickle

# Чтение
# with open('cities-europe.bin', 'rb') as file:
#     data = pickle.load(file)
# print(data)

# Преобразование
# bytestream = pickle.dumps(data)
# print(bytestream)
# normaldata = pickle.loads(bytestream)
# print(normaldata)

# Запись
# with open('countries.bin', 'wb') as file:
#     pickle.dump(data, file)

# Задание
with open('cities-europe.bin', 'rb') as file:
    data = pickle.load(file)
cities = list(data)
city_1 = []
city_2 = []
city_3 = []
city_4 = []
city_5 = []
for i in data:
    count = 0
    for j in i:
        if j.isupper():
            count += 1
    if count == 1:
        city_1.append(i)
print(len(city_1))
for i in city_1:
    b = i.lower()
    if b[0] == b[-1]:
        city_2.append(i)
print(len(city_2))
for i in city_2:
    glas = 'aeiouy'
    if i[1] in glas and i[1] == i[-2]:
        city_3.append(i)
print(len(city_3))
for i in city_3:
    for j in i:
        if j == 'w':
            city_4.append(i)
            break
for i in city_4:
    city_5.append(len(i))
print(min(filter(None, city_4), key=len))
