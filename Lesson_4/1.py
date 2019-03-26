"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

from random import randint
from timeit import timeit
import cProfile


def min_max_self(size=None):
    '''
    Расчет максимального значения из минимальных значений 
    в столбцах матрицы без исползования методов списков и словарей. 
    Вывод значений убран.
    '''
    matrix = []
    
    '''
    Вложенные циклы генерации массива размером size*size (квадратная матрица) имеют 
    квадратичную сложность O(n^2), при генерации массива размером 100*100, 
    в отчете модуля cProfile количество вызовов метода randint модуля 
    random и метода append списков примерно равны 100*100=10000
    '''
    tmp = []
    for _ in range(size):
        tmp = []
        for _ in range(size):
            tmp.append(randint(0, 100))
        matrix.append(tmp)  
    
    values = []
    
    '''
    Аналогичную сложность O(n^2) имееют вложенные циклы поиска минимального
    значения элементов в столбцах массива, совершается проход по всем элементам
    массива
    '''
    for i in range(size):
        min_val = None
        for j in range(size):
            if min_val is None or min_val > matrix[j][i]:
                min_val = matrix[j][i]
        values.append(min_val)
    
    '''
    Поиск масимального значения из списка минимальных значений имеет 
    линейную сложность O(n), проход осуществляется по всем 
    элементам списка (одномерная матрица)
    '''
    max_val = None
    for i in values:
        if max_val is None or max_val < i:
            max_val = i


def min_max_method(size=None):
    '''
    Рассчет максимального значения из минимальных значений 
    в столбцах матрицы с исползованием методов списков и словарей.
    Используются генератор списков и транспонирование матрицы.
    Вывод значений убран.
    '''
    
    '''
    При генерации массива размером size*size (квадратная матрица) с помощью генераторов
    списка количество вызовов метода randint модуля random остается на прежнем 
    уровне 100*100 = 10000, но не происходит вызовов метода append
    '''
    matrix = [[randint(0, 100) for _ in range(size)] for _ in range(size)]
    matrix_t = list(zip(*matrix))
    
    '''
    После транспонирования матрицы и использования функции поиска минимального
    значения в списке min сложность поска снизилась до линейной O(n), количество
    вызовов функции min равно количеству элементов массива
    ''' 
    min_val = []
    for n in range(size):
        min_val.append(min(matrix[n]))
    
    '''
    Поиск максимального значения в списке (одномерная матрица) функцией max
    имеет сложность O(1)
    '''
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

cProfile.run('run_self(size)')
cProfile.run('run_method(size)')
