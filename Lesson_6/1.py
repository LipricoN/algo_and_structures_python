"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile
from random import randint
from timeit import timeit

@profile
def min_max_self(size=None):
    matrix = []

    tmp = []
    for _ in range(size):
        tmp = []
        for _ in range(size):
            tmp.append(randint(0, 100))
        matrix.append(tmp)  
    
    values = []
    
    for i in range(size):
        min_val = None
        for j in range(size):
            if min_val is None or min_val > matrix[j][i]:
                min_val = matrix[j][i]
        values.append(min_val)
    
    max_val = None
    for i in values:
        if max_val is None or max_val < i:
            max_val = i

@profile
def min_max_method(size=None):
    matrix = [[randint(0, 100) for _ in range(size)] for _ in range(size)]
    matrix_t = list(zip(*matrix))
    
    min_val = []
    for n in range(size):
        min_val.append(min(matrix[n]))
    
    max_val = max(min_val)
    

def run_self(size=None):
    min_max_self(size)

def run_method(size=None):
    min_max_method(size)
    
size = int(input('Введите размер матрицы: '))    

run_method(size)
time_self = timeit('run_self(size)', setup='from __main__ import run_self, size', number=1)
time_method = timeit('run_method(size)', setup='from __main__ import run_method, size', number=1)

print(f'Время выполнения функции без использования встроенных методов списков и словарей: {time_self}')
print(f'Время выполнения функции с использованием встроенных методов списков и словарей: {time_method}')