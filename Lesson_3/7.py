"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint 

mass = [randint(0, 100) for _ in range(randint(20, 100))]

print(f'Дан массив:\n\n'
      f'{mass}\n\n'
      f'Определить два наименьших элемента.\n')

min_val = None
for v in mass:
    if min_val is None or min_val > v:
        min_val = v

min_val_count = 0
for v in mass:
    if v == min_val:
        min_val_count += 1

pre_min_val = None

if min_val_count > 1:
    pre_min_val = min_val
else:
    mass.remove(min_val)
    for v in mass:
        if pre_min_val is None or pre_min_val > v:
            pre_min_val = v    

print(f'{min_val} и {pre_min_val} являются минимальными числами в массиве.')
