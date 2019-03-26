"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def cycle(counter):
    num = 1
    sub = 1
    if counter > 1:
        for n in range(1, counter):
            sub = sub / 2
            if n % 2 != 0:
                num = num - sub
            else:
                num = num + sub
    print(f'Сумма ({counter}) элементов последовательности равна {num}')


def recursion(counter, start_counter=None, cur_num=1, sub=0.5):
    if start_counter is None:
        start_counter = counter

    if counter == 1:
        print(f'Сумма ({start_counter}) элементов последовательности равна {cur_num}')
    else:
        cur_num = cur_num - sub
        sub = sub / -2
        counter = counter - 1
        return recursion(counter, start_counter, cur_num, sub)


if __name__ == '__main__':
    num = int(input('Введите число суммируемых элементов (n): '))
    print('<----------- Выполнение циклом ----------->')
    cycle(num)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(num)

