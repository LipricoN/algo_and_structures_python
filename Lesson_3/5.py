#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

mass = [randint(-30, 30) for _ in range(randint(30, 100))]

print(f'Дан массив:\n\n'
      f'{mass}\n\n'
      f'Найти минимальное отрицательное значение\n')

min_neg = None
val_ind = None
for n, v in enumerate(mass):
    if (min_neg is None and v < 0) or (v < 0 and min_neg > v):
        min_neg = v
        val_ind = n

if min_neg is None:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Минимальное отрицательное число в массиве {min_neg} находится на позиции с индексом {val_ind}')