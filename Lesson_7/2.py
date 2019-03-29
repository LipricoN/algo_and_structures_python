"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import uniform, randint
import timeit

def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        
        return orig_list

if __name__ == '__main__':
    mass = [round(uniform(0, 49), 2) for _ in range(randint(20, 100))]
    print(f'Исходный одномерный целочисленный массив:\n{mass}', end='\n\n')
    
    sorted_mass = merge_sort(mass)
    print(f'Отсортированный массив по убыванию:\n{sorted_mass}', end='\n\n')
    
    time = timeit.timeit("merge_sort(mass)", \
        setup="from __main__ import merge_sort, mass", number=10)
    print(f'Время выполнения сортировки: {time}')