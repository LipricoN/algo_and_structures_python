"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def cycle(digit, num):
    count = 0
    start_num = num

    while True:
        if num >= 10:
            tmp = num % 10
            num //= 10

            if tmp == digit:
                count += 1
        else:
            if num == digit:
                count += 1
                break
            else:
                break
    print(f'Цифра {digit} встречается {count} раз(а) в последовательности {start_num}')


def recursion(digit, num, count=0, start_num=None):
    if start_num is None:
        start_num = num

    if num < 10:
        if num == digit:
            count += 1
        print(f'Цифра {digit} встречается {count} раз(а) в последовательности {start_num}')

    else:
        tmp = num % 10
        num //= 10
        if tmp == digit:
            count += 1
        return recursion(digit, num, count, start_num)


if __name__ == '__main__':
    digit = int(input('Введите цифру для подсчета: '))
    num = int(input('Введите последовательность чисел: '))
    print('<----------- Выполнение циклом ----------->')
    cycle(digit, num)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(digit, num)


