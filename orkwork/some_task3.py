# Задача 2
# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковые значения некоторой
# характеристики, и возвращает True, если это так. Если значение характеристики
# для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Пример:
# ввод: values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#   print("same")
# else:
#   print("different")
#   вывод: same
# Пример 2:
# ввод: values = [1, 2, 3, 4]
# if same_by(lambda x: x % 2, values):
#   print("same")
# else:
#   print("different")
#   вывод: different

values = [0, 3, 10, 6]
# values = [0, 2, 10, 6]
# values = []

def same_by(func, val):
    k = map(func, val)
    return 1 not in k and val


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')