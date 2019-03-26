"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def cycle(count):
    summ = 0
    for n in range(1, count + 1):
        summ = summ + n

    formula = (count*(count + 1)) / 2

    if summ == formula:
        print(f'Для множества натуральных чисел 1, 2,...,{n} справедливо равенство 1+2+...+n = n(n+1)/2')
    else:
        print('Что-то пошло не так')


def recursion(count, summ=0, start_count=0):
    if start_count == 0:
        start_count = count

    if count == 0:
        formula = (start_count * (start_count + 1)) / 2
        if summ == formula:
            print(f'Для множества натуральных чисел 1, 2,...,{start_count} справедливо равенство 1+2+...+n = n(n+1)/2')
        else:
            print('Что-то пошло не так')
    else:
        summ = summ + count
        return recursion(count - 1, summ, start_count)


if __name__ == '__main__':
    count = int(input('Введите натуральное число n: '))
    print('<----------- Выполнение циклом ----------->')
    cycle(count)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(count)
