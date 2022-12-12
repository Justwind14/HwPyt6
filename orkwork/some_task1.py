# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение[1, 2, 2, 3] 

def set_interseption(list_a, list_b):
    return sorted([i for i in list_a if i in list_b])

print(set_interseption([1, 2, 3, 2, 0],[5, 1, 2, 7, 3, 2]))

