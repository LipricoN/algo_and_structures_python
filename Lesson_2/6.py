"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


def cycle(num):
    n = 0
    while n < 10:
        user_num = int(input(f'Попробуйте угадать число от 0 до 100 за {10 - n} попыток: '))
        if user_num == num:
            print(f'Вы угадали! Это число {num}')
            break
        elif user_num < num:
            print(f'Число {user_num} меньше загаданного')
        elif user_num > num:
            print(f'Число {user_num} больше загаданного')
        n += 1
    else:
        print(f'Вы не угадали, загаданное число {num}')


def recursion(num, user_num=None, count=10):
    if num == user_num:
        print(f'Вы угадали! Это число {num}')
    elif count == 0:
        print(f'Вы не угадали, загаданное число {num}')
    else:
        user_num = int(input(f'Попробуйте угадать число от 0 до 100 за {count} попыток: '))
        if user_num < num:
            print(f'Число {user_num} меньше загаданного')
        elif user_num > num:
            print(f'Число {user_num} больше загаданного')
        return recursion(num, user_num, count - 1)


if __name__ == '__main__':
    num = random.randint(0, 100)
    print('<----------- Выполнение циклом ----------->')
    cycle(num)
    print('\n<----------- Выполнение рекурсией ----------->')
    recursion(num)
