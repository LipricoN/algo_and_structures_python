"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def cycle(a, b, c):
    def summ(num):
        tmp_summ = 0
        while num > 10:
            tmp_summ += num % 10
            num //= 10
        tmp_summ += num
        return tmp_summ

    summ_a = summ(a)
    summ_b = summ(b)
    summ_c = summ(c)

    if summ_a > summ_b and summ_a > summ_c:
        print(f'Максимальная сумма цифр у числа {a} равна {summ_a}')
    elif summ_b > summ_a and summ_b > summ_c:
        print(f'Максимальная сумма цифр у числа {b} равна {summ_b}')
    elif summ_c > summ_a and summ_c > summ_b:
        print(f'Максимальная сумма цифр у числа {c} равна {summ_c}')
    else:
        print('Сумма хотя бы пары чисел максимальна и равна равна')


def recursion(a, b, c):
    def summ(num, start_num=None, summ_num=0):
        if start_num is None:
            start_num = num

        if num < 10:
            summ_num += num
            return summ_num
        else:
            summ_num += num % 10
            num //= 10
            return summ(num, start_num, summ_num)

    summ_a = summ(a)
    summ_b = summ(b)
    summ_c = summ(c)

    if summ_a > summ_b and summ_a > summ_c:
        print(f'Максимальная сумма цифр у числа {a} равна {summ_a}')
    elif summ_b > summ_a and summ_b > summ_c:
        print(f'Максимальная сумма цифр у числа {b} равна {summ_b}')
    elif summ_c > summ_a and summ_c > summ_b:
        print(f'Максимальная сумма цифр у числа {c} равна {summ_c}')
    else:
        print('Сумма хотя бы пары чисел максимальна и равна равна')


if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
    print('<----------- Выполнение циклом ----------->')
    cycle(a, b, c)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(a, b, c)
