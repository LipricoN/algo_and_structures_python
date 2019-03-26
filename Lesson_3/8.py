"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from random import randint
matrix = []

matrix.append(input('Введите значения элементов матрицы первой строки, разделенные пробелами: ').split())
matrix.append(input('Введите значения элементов матрицы второй строки, разделенные пробелами: ').split())
matrix.append(input('Введите значения элементов матрицы третьей строки, разделенные пробелами: ').split())
matrix.append(input('Введите значения элементов матрицы четвертой строки, разделенные пробелами: ').split())

#tmp = []
#for _ in range(4):
    #tmp = []
    #for _ in range(5):
        #tmp.append(randint(0, 100))
    #matrix.append(tmp)

summ_row = []
for j in range(5):
    summ_col = 0
    
    for i in range(4):
        summ_col += int(matrix[i][j])
    
    summ_row.append(summ_col)
        
matrix.append(summ_row)

print()

for i in range(5):
    for j in range(5):
        print(f'{matrix[i][j]:^10}', end='')
    
    if i == 3:
        print('\n------------------------------------------------')
    else:
        print('', end='\n\n')
        