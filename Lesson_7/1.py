"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint
import timeit

def sort_mass(mass):
    count_1 = len(mass)
    count_2 = 0
    while count_1 > 1:
        for n in range(len(mass) - count_2):
            if n < (len(mass)-1) and mass[n] < mass[n+1]:
                mass[n], mass[n+1] = mass[n+1], mass[n]
        count_2 += 1
        count_1 -= 1
    return mass

if __name__ == '__main__':
    mass = [randint(-100, 99) for _ in range(randint(20, 100))]
    print(f'Исходный одномерный целочисленный массив:\n{mass}', end='\n\n')
    
    sorted_mass = sort_mass(mass)
    print(f'Отсортированный массив по убыванию:\n{sorted_mass}', end='\n\n')
    
    time = timeit.timeit("sort_mass(mass)", \
        setup="from __main__ import sort_mass, mass", number=10)
    print(f'Время выполнения сортировки: {time}')