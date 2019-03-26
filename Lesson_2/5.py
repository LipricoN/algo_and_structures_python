"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def cycle():
    for n in range(32, 128):
        if (n - 31) % 10 != 0:
            print(f'{n:>3}-{chr(n):^3}', end=' ')
        else:
            print(f'{n}-{chr(n)}')


def recursion(num=32):
    if num == 127:
        print(f'{num}-{chr(num)}')

    else:
        if (num - 31) % 10 != 0:
            print(f'{num:>3}-{chr(num):^3}', end=' ')
        else:
            print(f'{num}-{chr(num)}')

        return recursion(num + 1)


if __name__ == '__main__':
    print('<----------- Выполнение циклом ----------->')
    cycle()
    print('\n\n<----------- Выполнение рекурсией ----------->')
    recursion()
