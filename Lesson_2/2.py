"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def cycle(num):
    old_num = num
    even = 0
    odd = 0
    while True:
        if num >= 10:
            digit = num % 10
            num //= 10
            if digit % 2 == 0:
                even += 1
            else:
                odd += 1
        elif num < 10:
            if num % 2 == 0:
                even += 1
                break
            else:
                odd += 1
                break

    print(f'В числе {old_num} четных цифр {even}, нечетных {odd}')


def recursion(num, old_num=None, even=0, odd=0):

    if old_num is None:
        old_num = num

    if num < 10:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        print(f'В числе {old_num} четных цифр {even}, нечетных {odd}')
    else:
        digit = num % 10
        num //= 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        return recursion(num, old_num, even, odd)


if __name__ == '__main__':
    num = int(input('Введите натуральное число: '))
    print('<----------- Выполнение циклом ----------->')
    cycle(num)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(num)
