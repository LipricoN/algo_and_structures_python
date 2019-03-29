"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint
import timeit

def find_mediana(mass, pos=None):
    less = 0
    great = 0
    equal = 0
    if pos is None:
        pos = 0
    
    for n in mass:
        if n < mass[pos]:
            less += 1
        elif n > mass[pos]:
            great += 1
        elif n == mass[pos]:
            equal += 1
    
    if abs(less - great) <= equal:
        return mass[pos], less, great, equal-1
    else:
        return find_mediana(mass, pos + 1)



if __name__ == '__main__':
    m = int(input('Введите натуральное число m для генерации массива 2m+1: '))
    
    mass = [randint(0, 100) for _ in range(2*m+1)]
    print(f'Одномерный целочисленный массив:\n{mass}', end='\n\n')
    
    mediana, less, great, equal = find_mediana(mass)
    print(f'Медианой для массива является {mediana}, {less} значение(я) меньше медианы, '
          f'{great} значение(я) больше медианы, {equal} значение(я) равны медиане.', end='\n\n')
    
    time = timeit.timeit("find_mediana(mass)", \
        setup="from __main__ import find_mediana, mass", number=10)
    print(f'Время поиска медианы: {time}')