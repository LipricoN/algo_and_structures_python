# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

size = randint(2, 6)
matrix = []

tmp = []
for _ in range(size):
    tmp = []
    for _ in range(size):
        tmp.append(randint(0, 100))
    matrix.append(tmp)

print('Дана матрица:\n')

for i in range(size):
    for j in range(size):
        print(f'{matrix[i][j]:^6}', end='')
    print('', end='\n\n')

print('Найти максимальный элемент среди минимальных элементов столбцов матрицы.\n')    

values = []

for i in range(size):
    min_val = None
    for j in range(size):
        if min_val is None or min_val > matrix[j][i]:
            min_val = matrix[j][i]
    values.append(min_val)

str_values = ', '.join(map(str, values))

max_val = None
for i in values:
    if max_val is None or max_val < i:
        max_val = i
print(f'Из минимальных значений в столбцах {str_values} максимальным является {max_val}.')
