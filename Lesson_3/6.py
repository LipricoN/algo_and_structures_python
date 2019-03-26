"""
6. В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

mass = [randint(0, 10) for _ in range(randint(10, 20))]

print(f'Дан массив:\n\n'
      f'{mass}\n\n'
      f'Найти сумму элементов между минимальным и максимальным значением, не включая их.\n')

min_val = None
max_val = None

for v in mass:
    if min_val is None or min_val > v:
        min_val = v
        
    if max_val is None or max_val < v:
        max_val = v

min_val_ind = mass.index(min_val)
max_val_ind = mass.index(max_val)

tmp_mass = mass.copy()
tmp_mass.reverse()

if min_val_ind < max_val_ind:
    max_val_ind = tmp_mass.index(max_val)
    max_val_ind = len(mass) - max_val_ind - 1
    
    start_range = min_val_ind + 1
    stop_range = max_val_ind    
else:
    min_val_ind = tmp_mass.index(min_val)
    min_val_ind = len(mass) - min_val_ind - 1
    
    start_range = max_val_ind + 1
    stop_range = min_val_ind    

print(f'Минимальное значение {min_val} находится в позиции с индексом {min_val_ind}.\n'
      f'Максимальное значение {max_val} находится в позиции с индексом {max_val_ind}.\n')

summ = 0
summ_txt = ''

if stop_range - start_range > 1:
    for n in range(start_range, stop_range):
        if n == start_range:
            summ_txt = summ_txt + str(mass[n])
        else:
            summ_txt = summ_txt + ', ' + str(mass[n])
        summ += mass[n]
    
    print(f'Сумма чисел {summ_txt} между минимальным и максимальным значением равна {summ}.')
else:
    print(f'Минимальное и максимальное значения находятся в смежных позициях.')
