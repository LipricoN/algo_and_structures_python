"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def cycle(num):
    old_num = num
    reverce_num = ''

    while True:
        if num >= 10:
            digit = num % 10
            num //= 10
            reverce_num = reverce_num + str(digit)
        else:
            reverce_num = reverce_num + str(num)
            break

    reverce_num = int(reverce_num)
    print(f'Обратное по порядку цифр числу {old_num} является {reverce_num}')


def recursion(num, old_num=None, reverce_num=''):

    if old_num is None:
        old_num = num

    if num < 10:
        reverce_num = reverce_num + str(num)
        reverce_num = int(reverce_num)
        print(f'Обратное по порядку цифр числу {old_num} является {reverce_num}')
    else:
        digit = num % 10
        num //= 10
        reverce_num = reverce_num + str(digit)
        return recursion(num, old_num, reverce_num)


if __name__ == '__main__':
    num = int(input('Введите натуральное число: '))
    print('<----------- Выполнение циклом ----------->')
    cycle(num)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(num)
