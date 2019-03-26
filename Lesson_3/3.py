#3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

mass = [randint(0, 100) for _ in range(randint(5, 20))]

print(f'Задан массив случайных целых чисел: \n'
      f'{mass}\n')

min = None
max = None
for i, n in enumerate(range(len(mass))):
    if min is None or min > mass[n]:
        min = mass[n]
    
    if max is None or max < mass[n]:
        max = mass[n]    

index_min = mass.index(min)
index_max = mass.index(max)

print(f'Максимальное число в массиве {max} расположено в ячейке с индексом {index_max}')
print(f'Минимальное число в массиве {min} расположено в ячейке с индексом {index_min}\n')

mass[index_min], mass[index_max] = mass[index_max], mass[index_min]

print(f'Меняем метами максимальное и минимальное числа в массиве: \n'
      f'{mass}')
